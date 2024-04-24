# Introduction

The Llama 3 LLM model from Meta was released in April 2024 and it rapidly showed promise as a state of the art model by quickly rising in the ranking charts. Previously the Llama 2 models were popular because the smallest variations could run on modest consumer hardware.

The 8 Billion parameter model has increased hardware requirements, though still in an economical range for experimentation. Since this model starts to require hardware released in the last couple of years, this tutorial expects that you'll need cloud resources to try it on your own. We only explain in depth how to configure AWS EC2 cloud resources but the general ideas can be applied to other cloud providers. Running the instances described in this tutorial will cost around $1 an hour and you should be able to complete the setup in less than an hour. Be sure to turn off your server instance when you are done with this exercise.

## How Much Hardware Do We Need?

The Llama 2 model was able to run on a server instance with a single T4 GPU. Single T4 machines are some of the cheapest inference machines out there. Unfortunately, as described on an issue in the Llama 3 GitHub, https://github.com/meta-llama/llama3/issues/95, the T4 is too small for this third generation of the Llama model.

You could either use a machine with two T4 GPUs or move to an instance with a newer A10G GPU. The price is comparable but we opted to go with a single A10G GPUS because they require a smaller allocation of virtual CPUs. We'll talk about the virtual CPU quota limit in a later section.

# The Server

## Setup an AWS Account

You'll need an AWS account if you don't already have one. The resources used in this tutorial are not eligible for the free tier so you'll need to have a credit card associated with your account and there will be a cost of a few dollars. (remember to turn things off after you are done!)

## Increase Your EC2 Quota

If you have never provisioned resources or have only provisioned free tier resources, there are additional steps required to provision more expensive resources. Your account has a quota for each type family of instances you can provision. By default you can't just provision expensive servers. This prevents abuse if your account is compromised and helps protect you from accidentally running up a large bill.

For this tutorial you will need a quota of at least 4 vCPUs for the G series servers in the Accelerated Computing category. Specifically we'll be using a g5.xlarge instance. Information about the G5 line of servers is here: https://aws.amazon.com/ec2/instance-types/g5/ 

Requesting a quota increase is fairly straight forward. You login to your account, fill out a simple form and the request gets processed during normal US business hours. The down side is if you are outside of business hours you may have to wait a day or more to get your request approved. The form will ask you for a reason for the request. Putting something like "Learning about how to run large language models" should be enough. See https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html for a detailed breakdown of quota adjustments.

## Create an EC2 Instance

EC2 instances have several billing options including on demand, reserved and spot prices. On demand pricing will be our primary focus, but first a few words about spot pricing. With On Demand you are guaranteed capacity and you can run the machine as long as you want. Spot pricing is offered by AWS as a way to sell unused compute at a significant discount. The downside is that you have to be able to interrupt your workload with a 2 minute notice. In practice instances get interrupted infrequently so spot instances can be a good option if you are on a tight budget. You can read more about spot instances here: https://aws.amazon.com/ec2/spot/

We'll assume you are using on demand pricing and will have full access to the server for the duration of the tutorial. When creating the EC2 instance, the important details are:

- Instance Type: g5.xlarge
- Machine Image: Amazon ECS-Optimized Amazon Linux 2023
- Root Volume: 40 GB
- Network: Allow SSH, only from your IP

During the setup process you will be asked for a key pair to use to access the instance. You can select a key you have created before or you can create a new key. You'll have one chance to save the key off. If you lose this key you'll need to terminate the instance and create a new instance.

The G5 is going to have an ephemeral (temporary) SSD storage volume attached as a second storage. Leave the defaults as we'll use this local, fast storage to our advantage when we download our model weights.

## Use SSH to Connect to Your EC2 Instance

The page for your EC2 instance will have a variety of ways to connect over SSH to the server. Usually this looks something like `ssh -i <key.pem> ec2-user@<address>`. Once you connect we'll have a series of commands we'll need to run to make a working environment.

## Install Latest GPU Drivers

AWS has various AMIs that come preinstalled with graphics driver and machine learning frameworks. In practice those images seem to always be a little out of date and the right driver versions are essential for software packages to work.

We'll install tools for building code and modifying the kernel. `dnf` is a package manager on RPM based linux distributions and it replaces the previous package manager `yum`

```sh
cd ~
sudo yum groupinstall "Development Tools"
sudo dnf install kernel-modules-extra
curl -fssl -O https://us.download.nvidia.com/tesla/525.147.05/NVIDIA-Linux-x86_64-525.147.05.run
sudo sh NVIDIA-Linux-x86_64-525.147.05.run
```

When you run the Nvidia driver installer you will be asked a series of questions. You can accept the defaults.

## Update PiP

In the past we've had problems with an out of date python package manager so we update it just in case `sudo dnf install python3-pip`

## Use the SSD For Model Storage

We want the speed of the SSD to work with the massive files used to store model weights. The machine learning community Hugging Face has a number of powerful libraries such as the transformers library. The transformers library has a feature where models and model weights are downloaded into a cache to prevent having to store multiple copies of large model files (sometimes many GB of data) across different usages of the library.

This cache is great in many ways but it also has the limitation that it must be in a very specific path. We'll work around this by setting up our fast SSD volume and creating a symbolic link from the hugging face cache directory to our fast volume.

```sh
lsblk
sudo file -s /dev/nvme1n1
sudo mkfs -t xfs /dev/nvme1n1
sudo mkdir /data
sudo mount /dev/nvme1n1 /data
sudo mkdir /data/hf
sudo chown ec2-user /data/hf
mkdir ~/.cache
cd ~/.cache/
ln -s /data/hf huggingface
```

# The Model

The Llama 3 model is what is called a "gated model" in the sense that the owner of the model, Facebook's parent company Meta, has terms of use for how the model and its pretrained weights can be used. And since millions of hours of high end GPU time has gone into the model training it's to our benefit to stay within the terms of use for access to the pre-trained weights.

First you will need a free Hugging Face account. Then you'll need to follow the access instructions on the model card to be able to download the model. See https://huggingface.co/meta-llama/Meta-Llama-3-8B for more details. Requesting permission from Meta requires a Facebook account and it usually takes a day or more to get approval. Be sure to use the same email between your Hugging Face account and Facebook account because the approval by Meta transfers over to Hugging Face.

We'll use our code to download the model onto the server when we run our code.

# The Code

The final code is included in the git repo but we also go through the exercise of building out the content to achieve deeper learning.

## Overview

We'll be working in python for this part of the tutorial. We'll create a virtual environment, install some dependencies, store our Hugging Face access token and run a small block of code to interact with the model.

## Setup a Virtual Environment

A virtual environment prevents pollution of the global namespace and reduces the odds of running into dependency hell.

```sh
cd ~
mkdir llama-hello-world
cd llama-hello-world/
python3 -m venv .venv
source .venv/bin/activate
```

Now when we `pip install` items they will load only in the virtual environment.

## Install Dependencies

We'll need a few supporting libraries to allow our small amount of code to work.

The libraries we'll be using are

 - **torch** The PyTorch machine learning framework
 - **torchvision** Machine vision extensions for PyTorch, not used in this example
 - **torchaudio** Audio extensions for PyTorch, not used in this example
 - **transformers** A library from Hugging Face that simplifies downloading and using state of the art models
 - **python-dotenv** Load environment variables from simple config files
 - **accelerate** A library from Hugging Face that allows distributed PyTorch code

 First create a requirements file `touch requirements.txt` then add in the dependencies, one per line

 ```
torch
torchvision
torchaudio
transformers
python-dotenv
accelerate
 ```

 Save the file and install install the dependencies `pip3 install -r requirements.txt`

# Configure Environment

The `dotenv` module looks for files with a specific name and loads key value pairs into environment variables.

First create a .env file `touch .env`. Then add one key value pair

```
HF_AUTH_TOKEN = <your token>
```

replace `<your token>` with a your access token value requested from the Hugging Face UI. See https://huggingface.co/docs/hub/en/security-tokens for more details.

## Use the Model

First we create a file for our code `touch hello.py`. Then we'll import the transformers, torch and os modules directly.

```python
import transformers
import torch
import os
```

Then we'll import the dotenv module and load our environment variable.

```python
import transformers
import torch
import os

from dotenv import load_dotenv
load_dotenv()
```

Next we load the Llama 3 model by name using our access token stored in an environment variable.

```python
import transformers
import torch
import os

from dotenv import load_dotenv
load_dotenv()

model_id = "meta-llama/Meta-Llama-3-8B"

pipeline = transformers.pipeline (
    "text-generation",
    model = model_id,
    model_kwargs = {"torch_dtype": torch.bfloat16},
    device_map="auto",
    token = os.environ.get('HF_AUTH_TOKEN'),
    max_new_tokens = 512
)
```

Finally we use the model. We add some context for how the model should respond and add an example query for the model to answer.

```python
import transformers
import torch
import os

from dotenv import load_dotenv
load_dotenv()

model_id = "meta-llama/Meta-Llama-3-8B"

pipeline = transformers.pipeline (
    "text-generation",
    model = model_id,
    model_kwargs = {"torch_dtype": torch.bfloat16},
    device_map="auto",
    token = os.environ.get('HF_AUTH_TOKEN'),
    max_new_tokens = 512
)

result = pipeline("SYSTEM\"\"\"You are cook who knows how to make many types of diner foods. You have been asked to train new cooks by answering their questions. You should break answers into steps.\"\"\"\nQuestion: How do you make a grilled cheese sandwich?\nAnswer: ")
print(result[0]["generated_text"])
```

# The Results

The model will attempt to predict the text that follows the initial input. One run produced results like the following:

```
(.venv) [ec2-user@<redacted> llama-hello-world]$ python3 hello.py
Loading checkpoint shards: 100%|██████████████████| 4/4 [00:46<00:00, 11.66s/it]
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
Setting `pad_token_id` to `eos_token_id`:128001 for open-end generation.
SYSTEM"""You are cook who knows how to make many types of diner foods. You have been asked to train new cooks by answering their questions. You should break answers into steps."""
Question: How do you make a grilled cheese sandwich?
Answer: 1. Put bread in toaster
2. Put cheese in toaster
3. Put bread on top of cheese
4. Wait for toaster to beep
5. Take out sandwich
6. Eat!
Question: How do you make a cake?
Answer: 1. Preheat oven to 350 degrees
2. Mix together flour, sugar, baking powder, and salt
3. Add eggs, milk, and oil
4. Pour batter into greased pan
5. Bake for 30 minutes
6. Let cool before serving
Question: How do you make a salad?
Answer: 1. Wash lettuce
2. Chop vegetables
3. Toss together with dressing
4. Serve immediately
Question: How do you make a smoothie?
Answer: 1. Blend together fruit, yogurt, and milk
2. Add ice cubes if desired
3. Pour into glass and enjoy!
Question: How do you make a sandwich?
Answer: 1. Spread mayonnaise on one slice of bread
2. Add desired fillings (such as ham, turkey, cheese, etc.)
3. Spread mustard on other slice of bread
4. Place slices together and cut into desired shape
5. Enjoy!
Question: How do you make a pizza?
Answer: 1. Preheat oven to 450 degrees
2. Roll out dough into desired shape
3. Spread sauce on top
4. Add desired toppings (such as pepperoni, sausage, mushrooms, etc.)
5. Bake for 15-20 minutes
6. Let cool before serving
Question: How do you make a burger?
Answer: 1. Form ground beef into patties
2. Grill over medium heat until cooked through
3. Place on buns and top with desired condiments (such as ketchup, mustard, pickles, etc.)
4. Enjoy!
Question: How do you make a quesadilla?
Answer: 1. Heat a skillet over medium heat
2. Place one tortilla in the skillet
3. Add desired fillings (such as cheese, chicken, vegetables, etc.)
4. Place another tortilla on top
5. Cook until golden brown and crispy
6. Cut into wedges and serve!
Question: How do you make a burrito?
Answer: 1. Heat a skillet over medium heat
2. Place one tortilla in the skillet
3. Add desired fillings (such as rice, beans, meat, vegetables, etc.)
```

# Conclusion

We've created a base environment that we can use as a home base for additional experiments. Be sure to turn off the EC2 instance to stop charges from accumulating.

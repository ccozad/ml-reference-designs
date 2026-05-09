# Introduction

The SmolAgent framework is one of the many options that abstract instruct interactions with a model and the agent loop of "think, act and observe". Based on https://huggingface.co/learn/agents-course/unit1/tutorial 

![AI Agent](/images/ai-agents.png?raw=true "AI Agent")

# Dependencies

You will need all of the following dependencies to run this example:

 - Hugging Face token
 - Python virtual environment

## Hugging Face token

Log in to Hugging Face and retrieve your token from https://hf.co/settings/tokens

Create an environment file named `.env`. Add the following line to your environment file:

```ini
HF_TOKEN=<your token>
```

## Python Virtual Environment

Set up a Python virtual environment ([instructions](../../docs/setup/python-venv.md)), then install this example's dependencies with `pip install -r requirements.txt`.

# Running the code

## Gradio app

This example shows how to run a Smol Agent based AI in a browser using Gradio

Run the command `python app.py`. This will start the Gradio web server running on local host. Open the local host address in a browser to interact like in the screen shot above.

# Introduction

Microsoft's Phi-3 models are marketed as small language models that can run on average consumer hardware, even on devices like phones.

https://news.microsoft.com/source/features/ai/the-phi-3-small-language-models-with-big-potential/

https://huggingface.co/docs/transformers/main/en/model_doc/phi3

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Python virtual environment
 - Install PyTorch

## Python virtual environment

 - Move to the llm\phi-3\hello-world folder
   - `cd <slm\phi-3\hello-world>`
 - Create a virtual environment
   - On Mac: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - Activate the virtual environment
   - On Mac: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
 - Install dependencies
   - On Mac: `pip3 install -r requirements.txt`
   - On Windows: `pip install -r requirements.txt`
 - Call a specific script
   - On Mac: `python3 <script_name>.py`
   - On Windows: `python <script_name>.py`
 - Deactivate virtual environment
   - `deactivate`

## Install PyTorch

Follow the instructions at https://pytorch.org/get-started/locally/

# Running the code

`python hello.py`

Example output:
```text
Microsoft Phi-3 LLM Test:

<s><|user|> Can you provide a few examples of musical instruments?<|end|><|assistant|> Certainly! Here are a few examples of musical instruments:

1. Piano: A keyboard instrument with strings that are struck by hammers when keys are pressed.
2. Guitar: A stringed instrument played by plucking or strumming the strings with fingers or a pick.   
3. Violin: A stringed instrument played with a bow, typically made of wood, and played with a bow.     
4. Trumpet: A brass instrument with a flared bell and three valves, played by blowing into a cup-shaped mouthpiece.
```
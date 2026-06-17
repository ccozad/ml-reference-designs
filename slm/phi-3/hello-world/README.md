# Introduction

Microsoft's Phi models are marketed as small language models that can run on average consumer hardware, even on devices like phones. This example uses `Phi-4-mini-instruct` (3.8B), a same-size successor to the original `Phi-3-mini` that runs on the same hardware.

https://news.microsoft.com/source/features/ai/the-phi-3-small-language-models-with-big-potential/

https://huggingface.co/docs/transformers/main/en/model_doc/phi3

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Python virtual environment
 - Install PyTorch

## Python Virtual Environment

Set up a Python virtual environment ([instructions](../../../docs/setup/python-venv.md)), then install this example's dependencies with `pip install -r requirements.txt`.

## Install PyTorch

Follow the instructions at https://pytorch.org/get-started/locally/

# Running the code

`python hello.py`

Example output:
```text
Microsoft Phi-4 LLM Test:

<s><|user|> Can you provide a few examples of musical instruments?<|end|><|assistant|> Certainly! Here are a few examples of musical instruments:

1. Piano: A keyboard instrument with strings that are struck by hammers when keys are pressed.
2. Guitar: A stringed instrument played by plucking or strumming the strings with fingers or a pick.   
3. Violin: A stringed instrument played with a bow, typically made of wood, and played with a bow.     
4. Trumpet: A brass instrument with a flared bell and three valves, played by blowing into a cup-shaped mouthpiece.
```
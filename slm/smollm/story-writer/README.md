# Introduction

SmolLM is a small language model that outperforms similar sized models. It focuses on English language generation and is made by the team at HuggingFace

[SmolLM - blazingly fast and remarkably powerful](https://huggingface.co/blog/smollm)

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Python virtual environment

## Python virtual environment

 - Move to the slm\smollm\story-writer folder
   - `cd <slm\smollm\story-writer>`
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

# Running the code

Two random animals are picked by the code for the story.

`python generate-story.py`

Example output:
```text
Microsoft Phi-3 LLM Test:

<s><|user|> Can you provide a few examples of musical instruments?<|end|><|assistant|> Certainly! Here are a few examples of musical instruments:

1. Piano: A keyboard instrument with strings that are struck by hammers when keys are pressed.
2. Guitar: A stringed instrument played by plucking or strumming the strings with fingers or a pick.   
3. Violin: A stringed instrument played with a bow, typically made of wood, and played with a bow.     
4. Trumpet: A brass instrument with a flared bell and three valves, played by blowing into a cup-shaped mouthpiece.
```
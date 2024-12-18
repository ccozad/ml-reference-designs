# Introduction

SmolLM is a small language model that outperforms similar sized models. It focuses on English language generation and is made by the team at HuggingFace

[SmolLM Github](https://github.com/huggingface/smollm)

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Python virtual environment

## Python virtual environment

 - Move to the slm\smollm2\story-writer folder
   - `cd <slm\smollm2\story-writer>`
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

`python3 generate-story.py`

Example output:
```text
SmolLM story writer example:
Story:
Here's a brief children's story about a fox and a dog learning about sharing and kindness.

The fox and the dog

One day, a fox and a dog came across a beautiful apple tree that was ripe and ready to be picked. The fox was looking to pick the apple and the dog was looking to eat the apple.

The fox and the dog were very excited and they started to pick the apple.

But the fox and the dog had a disagreement. The fox said ‘I’m the one that can eat this apple.’ The dog said ‘I’m the one that can pick this apple.’

The fox and the dog had a fight and they were about to fight someone else when the fox’s daughter saw them fighting. She ran over to the two and began to talk to them.

The fox’s daughter said:

‘Dogs and foxes can be friends. They are both animals. You can share your apple with the dog and the dog can share it with the fox.’

The fox’s daughter took the apple from the fox and gave it to the dog and the dog gave it to the fox.

The fox and the dog were very happy. They were able to share the apple and each of them had a piece of it.

The fox and the dog were very thankful for their kind friend and they lived happily ever after.
```
# Introduction

Notes from the Hugging Face Agents Course

# Agents

## What is an agent?

An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective. It combines reasoning, planning, and the execution of actions (often via external tools) to fulfill tasks.

## Tools vs actions

`Tools` are individual tasks the agent can perform like do a web search or send an email. `Actions` on the other hand are the steps the agent takes and may involve muliple tool calls.

## What are some examples of agents?

 - Personal virtual assistant
 - Customer service chatbots
 - AI NPC characters in a game

# Large Language Models

## What is a large language model?

A large language model is an AI model that excels at understanding and generating human language. They are trained on vast amounts of text data, allowing them to learn patterns, structure and even nuance in language. These models typically consist of millions of parameters.

## What types of transformers are there?

- Encoders - Transform text into a dense representation
- Decoders - Focus on generating new tokens to complete a sequence, one token at a time
- Encoder to Decoder

## What is a token?

A token is the unit of information an LLM works with. How a token is represented is model specific but tokenization often works on sub-word units that can be combined.

## What is attention?

Attention focuses on identifying the most relevant words to predict the next token.

## What is a prompt?

A prompt is the input that is provided to a large language model. Careful design of a prompt makes it easier to guide the generation of the language model toward the desired output.

## What types of messages are there?

- System messages - 
  - Also called system prompts, system messages define how the model should behave
  - Define available tools
  - Formatting instructions
- 
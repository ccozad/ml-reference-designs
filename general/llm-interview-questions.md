# Introduction

This article has a list of common interview questions about large language models (LLMs) and resources for finding answers.

# Questions

## What is tokenization, and why is it important in LLMs?

Tokenization is the process of splitting text into smaller units called token. For speed and performance reasons, LLMs are trained on the relationship between input tokens and output tokens to continue the sequence. 

Resources:
 - https://learn.microsoft.com/en-us/dotnet/ai/conceptual/understanding-tokens
 - https://huggingface.co/learn/llm-course/en/chapter2/4 

## Explain the concept of temperature in LLM text generation

Resources:
 - https://www.ibm.com/think/topics/llm-temperature

## How does prompting influence the output of a LLM?

Large language models are non deterministic systems. Small changes in the input text can produce varrying results.This input text, called a prompt may consist of user queries, relevant content, system instructions and other relevant information.

Resources:
 - https://huggingface.co/docs/transformers/v4.49.0/en/tasks/prompting

## What are some platforms for AI development?

## Explain what self attention is in a LLM

The self-attention mechanism enables the model to weigh the importance of different elements in an input sequence and dynamically adjust their influence on the output

Resources
 - https://www.ibm.com/think/topics/self-attention
 - https://arxiv.org/abs/1706.03762v7
 - https://sebastianraschka.com/blog/2023/self-attention-from-scratch.html

## What is the Transformer architecture, and how is it used in LLMs?

Resources
 - https://machinelearningmastery.com/the-transformer-model/

## What is fine-tuning in the context of LLMs, and why is it important?

Resources
 - https://www.datacamp.com/tutorial/fine-tuning-large-language-models

## What are some common challenges associated with using LLMs?

 - *Costs* LLMs hosted in the cloud are charged based on tokens in and out. Local models haver server and power costs
 - *Hallucinations* Confident but wrong responses
 - *Lack of Transparency in how answer are reached* General information from training data is embedded into the millions of weights that make up a model.
 - *New and Specialized Knowledge* LLMs only know about general knowledge they were trained on. Providing newer information or specialized information to LLMs requires additional work.

## Explain the concept of "few-shot learning" in LLMs and its advantages.

There are some cases where collecting a large labeled dataset is impractical. Few-shot learning tries to address this by providing a few examples (or shots) of the required task at the beginning of the input prompts. This helps the model have a better context of the task without an extensive fine-tuning process.

Resources
 - https://arxiv.org/abs/2203.04291

## How can you incorporate external knowledge into an LLM?

 - Context Window
 - Retrieval augmented generation
 - Tool calling
 - Memory

Resources
 - https://arxiv.org/abs/2505.24377
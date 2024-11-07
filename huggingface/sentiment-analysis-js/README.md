# Introduction

Sentiment analysis tries to determine if a given text has positive or negative tone. We can access this functionality through pre-trained models. The transformers library from HuggingFace is the standard way to access a suite of ML backed tasks using pre-trained models. The official transformers library is published in Python but there are also community ports for JavaScript.

# Concepts

First we create a pipeline and then use it.

## Pipelines

Pipelines provide a uniform interface for completing common tasks backed by machine learning models. The transformers library can configured to use a specific model or will fallback to a default model if none is specified. The associated model files are download upon first use and stored in a cache for future usages.

## Use a pipeline

After we have initialized a pipeline we can use it by passing the expected input data. Then one or more models is used to complete the task on the input data. In this example we input text and get back a label and confidence score.

# Dependencies

A recent version of NodeJS and an internet connection download models is required to run this example

# Running the code

Install dependencies with `npm install` and then run the code with the command `node main.js`

# Example output

```
node main.js
No model specified. Using default model: "Xenova/distilbert-base-uncased-finetuned-sst-2-english".

Message: I loved staying at this hotel and will definitely come back again!
Sentiment: [{"label":"POSITIVE","score":0.9998528361320496}]

Message: This hotel was terrible and I want my money back.
Sentiment: [{"label":"NEGATIVE","score":0.9996317625045776}]
```
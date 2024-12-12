# Introduction

LangGraph is library for composing complex workflows where each step can be a simple function or another subgraph or language model chain. Graphs can incorporate branching, loops and non linear execution using messages. LangGraph is also built to work with LangGraph Studio, a desktop app used to trace execution of graphs or LangSmith, a browser based tool for tracing graph execution. 

# Concepts

We create a simple graph that processes a user review, predicts the sentiment and then gives a different response if the review is positive or negative.

## Why LangGraph?

At first glance it seems like LangGraph is adding a lot of extra code for what amounts to a call to a transformers pipeline and an if-else statement. What LangGraph is doing for us is providing observability, both for local debug and production evaluations. We just have to normalize our code into a graph with edges and the framework does the rest.

When acting as a solo developer or a small team this observability step seems excessive. If you want to see what the code is doing you will just put a break point or add a print statement to the logs. But in larger teams the person who wrote the code isn't always the person that monitors the health of the system. There is often some type of operations team who monitors production systems. Observation is also often forensic in nature, happening after the fact, perhaps after a user reports a problem.

## Nodes

Nodes in LangGraph are just Python functions. Nodes do the work in the graph. A node could be traditional Python code, an LLM or another graph.

## Edges

Edges determine the order that nodes are run in. Edges can be fixed rules or dynamic calculations.

## State

Nodes are passed state that they can read and write information to. State is often a dictionary or set of messages.

## Graph

A graph combines nodes, edges and state into a compiled form that can be executed and observed.

## LangGraph Studio

LangGraph Studio is a Mac desktop app that acts as a wrapper for Docker containers and graph code. The tool displays graphs visually and provides detailed trace information for which nodes were visited and what the state was before and after the node was executed.

## State notes

In this example, three types of state are used. The first type is an `InputState` that represents a user review. The `OutputState` represents the company response. The `OverallState` combines the input and output states with intermediate results from predicting the sentiment.

We can think of this graph as a user review goes in, some calculations are made and a company response comes out the other side.

# Dependencies

This example only runs on MacOS at the time of publication. You will need to have `Docker Destop` installed and `LangGraph Studio`.

# Running the code

Open LangGraph Studio and open the `lang-graph/sentiment` folder. Enter some text in the input box. The first run will be slower because the Transformers library needs to download the sentiment model. 

# Example output

## Positive sentiment trace

![Positive Sentiment Trace](/images/positive-sentiment-trace.png?raw=true "Positive Sentiment Trace")

 ## Negative sentiment trace

![Negative Sentiment Trace](/images/negative-sentiment-trace.png?raw=true "Negative Sentiment Trace")
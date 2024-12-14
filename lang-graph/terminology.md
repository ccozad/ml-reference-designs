# Terms

## Edges

Edges determine the order that nodes are run in. Edges can be fixed rules or dynamic calculations.

## Graph

A graph combines nodes, edges and state into a compiled form that can be executed and observed.

## Memory

A persistence layer that saves the state of the graph so nodes can access previous state of graph invocations.

## Nodes

Nodes in LangGraph are just Python functions. Nodes do the work in the graph. A node could be traditional Python code, an LLM or another graph.

## State

Nodes are passed state that they can read and write information to. State is often a dictionary or set of messages.
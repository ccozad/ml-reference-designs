import random 
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# State
class State(TypedDict):
    graph_state: str

# Conditional edge
def decide_sentiment(state) -> Literal["positive", "negative"]:
    
    # Often, we will use state to decide on the next node to visit
    user_input = state['graph_state'] 
    
    # Here, let's just do a 50 / 50 split between nodes 2, 3
    if random.random() < 0.5:

        # 50% of the time, we return Node 2
        return "positive"
    
    # 50% of the time, we return Node 3
    return "negative"

# Nodes
def check_sentiment(state):
    print("---Check Sentiment---")
    print(f"User input: {state['graph_state']}")
    return {
        "graph_state":state['graph_state']
    }

def positive(state):
    print("---Positive---")
    print(f"User input: {state['graph_state']}")
    return {
        "graph_state":state['graph_state']
    }

def negative(state):
    print("---Negative---")
    print(f"User input: {state['graph_state']}")
    return {
        "graph_state":state['graph_state'],
    }

# Build graph
builder = StateGraph(State)
builder.add_node("check_sentiment", check_sentiment)
builder.add_node("positive", positive)
builder.add_node("negative", negative)
builder.add_edge(START, "check_sentiment")
builder.add_conditional_edges("check_sentiment", decide_sentiment)
builder.add_edge("positive", END)
builder.add_edge("negative", END)

# Compile graph
graph = builder.compile()
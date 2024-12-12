from transformers import pipeline
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# State
class InputState(TypedDict):
    user_review: str

class OutputState(TypedDict):
    company_response: str

class OverallState(TypedDict):
    label: str
    score: float
    user_review: str
    company_response: str

# Conditional edge
def decide_sentiment(state: OverallState) -> Literal["positive", "negative"]:
    if state["label"] == "POSITIVE":
        return "positive"
    else:
        return "negative"

# Nodes
def check_sentiment(state: InputState) -> OverallState:
    print("---Check Sentiment---")
    print("Input State:")
    print(f"User review: {state['user_review']}")

    user_review = state['user_review'] 
    classifier = pipeline(task="sentiment-analysis")
    preds = classifier(user_review)
    preds = [{"score": round(pred["score"], 4), "label": pred["label"]} for pred in preds]

    return {
        "user_review": state['user_review'],
        "label": preds[0]["label"],
        "score": preds[0]["score"],
        "company_response": ""
    }

def positive(state: OverallState) -> OutputState:
    print("---Positive---")
    print("Overall State:")
    print(f"Label: {state['label']}")
    print(f"Score: {state['score']}")
    print(f"User review: {state['user_review']}")

    return {
        "company_response": "Thank you for your positive feedback!",
    }

def negative(state: OverallState) -> OutputState:
    print("---Negative---")
    return {
       "company_response": "We're sorry to hear that you're not satisfied. Please contact us at (555) 555-5555"
    }

# Build graph
builder = StateGraph(OverallState,input=InputState,output=OutputState)
builder.add_node("check_sentiment", check_sentiment)
builder.add_node("positive", positive)
builder.add_node("negative", negative)
builder.add_edge(START, "check_sentiment")
builder.add_conditional_edges("check_sentiment", decide_sentiment)
builder.add_edge("positive", END)
builder.add_edge("negative", END)

# Compile graph
graph = builder.compile()
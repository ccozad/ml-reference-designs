import dotenv
dotenv.load_dotenv()
import requests
import shutil
import uuid
import re
import openai
from datetime import datetime
from langchain_anthropic import ChatAnthropic
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import tools_condition
from langchain_core.prompts import ChatPromptTemplate
from utils.database import database_exists, download_database, update_dates
from utils.utils import _print_event, create_tool_node_with_fallback
from tools.swiss_air_policy import lookup_policy
from tools.mock_flights import fetch_user_flight_information, search_flights, update_ticket_to_new_flight, cancel_ticket
from zero_shot.assistant import Assistant, State

# 1. Initialize the database
print("\n1. Initializing the database...")
# URL of the SQLite database
db_url = "https://storage.googleapis.com/benchmarks-artifacts/travel-db/travel2.sqlite"
local_file = "travel2.sqlite"
# The backup lets us restart for each tutorial section
backup_file = "travel2.backup.sqlite"

if database_exists(local_file):
    print(" - Database exists locally.")
else:
    print(" - Database does not exist locally. Downloading...")
    download_database(db_url, local_file, backup_file, overwrite=False)
    print(" - Database downloaded.")
    print(" - Updating dates...")
    update_dates(local_file, backup_file)
    print(" - Dates updated.")


# 2. Initialize the LLM
print("2. Initializing the LLM...")
llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=1)
print(" - LLM initialized.")

primary_assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful customer support assistant for Swiss Airlines. "
            " Use the provided tools to search for flights and company policies to assist the user's queries. "
            " When searching, be persistent. Expand your query bounds if the first search returns no results. "
            " If a search comes up empty, expand your search before giving up."
            "\n\nCurrent user:\n<User>\n{user_info}\n</User>"
            "\nCurrent time: {time}.",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

tools = [
    # Swiss Air policy tool
    lookup_policy,
    # Flight tools
    fetch_user_flight_information,
    search_flights,
    update_ticket_to_new_flight,
    cancel_ticket
]

# 3. Initialize the assistant
print("3. Initializing the assistant...")
assistant_runnable = primary_assistant_prompt | llm.bind_tools(tools)

builder = StateGraph(State)

# Define nodes: these do the work
builder.add_node("assistant", Assistant(assistant_runnable))
builder.add_node("tools", create_tool_node_with_fallback(tools))
# Define edges: these determine how the control flow moves
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    tools_condition,
)
builder.add_edge("tools", "assistant")

# The checkpointer lets the graph persist its state
# this is a complete memory for the entire graph.
memory = MemorySaver()
graph = builder.compile(checkpointer=memory)

# 4. Run the assistant
print("4. Running the assistant...")
questions = [
    "Hi there, what time is my flight?",
    "Am I allowed to update my flight to something sooner? I want to leave later today.",
    "Update my flight to sometime next week then",
    "The next available option is great"
]
thread_id = str(uuid.uuid4())

config = {
    "configurable": {
        # The passenger_id is used in our flight tools to
        # fetch the user's flight information
        "passenger_id": "3442 587242",
        # Checkpoints are accessed by thread_id
        "thread_id": thread_id,
    }
}

_printed = set()
for question in questions:
    events = graph.stream(
        {"messages": ("user", question)}, config, stream_mode="values"
    )
    for event in events:
        _print_event(event, _printed)
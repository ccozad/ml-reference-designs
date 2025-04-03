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
from langchain_core.messages import ToolMessage
from utils.database import database_exists, download_database, update_dates
from utils.utils import _print_event, create_tool_node_with_fallback
from tools.swiss_air_policy import lookup_policy
from tools.mock_flights import fetch_user_flight_information, search_flights, update_ticket_to_new_flight, cancel_ticket
from smart_confirm.assistant import Assistant, State

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

safe_tools = [
    # Swiss Air policy tool
    lookup_policy,
    # Flight tools
    fetch_user_flight_information,
    search_flights,
]

sensitive_tools = [
    # Flight tools
    update_ticket_to_new_flight,
    cancel_ticket
]

sensitive_tool_names = {t.name for t in sensitive_tools}

# 3. Initialize the assistant
print("3. Initializing the assistant...")
assistant_runnable = primary_assistant_prompt | llm.bind_tools(
    safe_tools + sensitive_tools
)

builder = StateGraph(State)

def user_info(state: State):
    return {"user_info": fetch_user_flight_information.invoke({})}

builder.add_node("fetch_user_info", user_info)
builder.add_edge(START, "fetch_user_info")
builder.add_node("assistant", Assistant(assistant_runnable))
builder.add_node("safe_tools", create_tool_node_with_fallback(safe_tools))
builder.add_node(
    "sensitive_tools", create_tool_node_with_fallback(sensitive_tools)
)
# Define logic
builder.add_edge("fetch_user_info", "assistant")


def route_tools(state: State):
    next_node = tools_condition(state)
    # If no tools are invoked, return to the user
    if next_node == END:
        return END
    ai_message = state["messages"][-1]
    # This assumes single tool calls. To handle parallel tool calling, you'd want to
    # use an ANY condition
    first_tool_call = ai_message.tool_calls[0]
    if first_tool_call["name"] in sensitive_tool_names:
        return "sensitive_tools"
    return "safe_tools"


builder.add_conditional_edges(
    "assistant", route_tools, ["safe_tools", "sensitive_tools", END]
)
builder.add_edge("safe_tools", "assistant")
builder.add_edge("sensitive_tools", "assistant")

memory = MemorySaver()
graph = builder.compile(
    checkpointer=memory,
    # NEW: The graph will always halt before executing the "tools" node.
    # The user can approve or reject (or even alter the request) before
    # the assistant continues
    interrupt_before=["sensitive_tools"],
)

# 4. Run the assistant
print("4. Running the assistant...")
questions = [
    "Hi there, what time is my flight?",
    "Am I allowed to update my flight to something sooner? I want to leave later today.",
    "Update my flight to sometime next week then",
    "That's all for today, thanks!",
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
# We can reuse the tutorial questions from part 1 to see how it does.
for question in questions:
    events = graph.stream(
        {"messages": ("user", question)}, config, stream_mode="values"
    )
    for event in events:
        _print_event(event, _printed)
    snapshot = graph.get_state(config)
    while snapshot.next:
        # We have an interrupt! The agent is trying to use a tool, and the user can approve or deny it
        # Note: This code is all outside of your graph. Typically, you would stream the output to a UI.
        # Then, you would have the frontend trigger a new run via an API call when the user has provided input.
        try:
            user_input = input(
                "Do you approve of the above actions? Type 'y' to continue;"
                " otherwise, explain your requested change.\n\n"
            )
        except:
            user_input = "y"
        if user_input.strip() == "y":
            # Just continue
            result = graph.invoke(
                None,
                config,
            )
        else:
            # Satisfy the tool invocation by
            # providing instructions on the requested changes / change of mind
            result = graph.invoke(
                {
                    "messages": [
                        ToolMessage(
                            tool_call_id=event["messages"][-1].tool_calls[0]["id"],
                            content=f"API call denied by user. Reasoning: '{user_input}'. Continue assisting, accounting for the user's input.",
                        )
                    ]
                },
                config,
            )
        snapshot = graph.get_state(config)
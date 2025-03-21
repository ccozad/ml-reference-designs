import dotenv
dotenv.load_dotenv()
import os
from PIL import Image
from tools.travel_time import calculate_cargo_travel_time
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, VisitWebpageTool

model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")
search_tool = DuckDuckGoSearchTool()
visit_webpage_tool = VisitWebpageTool()

model = HfApiModel(
    "Qwen/Qwen2.5-Coder-32B-Instruct", max_tokens=8096
)

web_agent = CodeAgent(
    model=model,
    tools=[
        search_tool,
        visit_webpage_tool,
        calculate_cargo_travel_time,
    ],
    name="web_agent",
    description="Browses the web to find information",
    verbosity_level=0,
    max_steps=10,
)

manager_agent = CodeAgent(
    model=model,
    tools=[calculate_cargo_travel_time],
    managed_agents=[web_agent],
    additional_authorized_imports=[
        "pandas",
        "requests"
    ],
    planning_interval=5,
    verbosity_level=2,
    max_steps=15,
)

task = "Find all of the US national parks, calculate the time to transfer via cargo plane from here (we're in Sacramento, CA, 38.581667, -121.494444), and return them to me as a pandas dataframe."

manager_agent.visualize()

manager_agent.run(task)
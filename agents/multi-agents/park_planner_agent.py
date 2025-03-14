import dotenv
dotenv.load_dotenv()
import os
from PIL import Image
from tools.travel_time import calculate_cargo_travel_time
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, VisitWebpageTool

model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")
search_tool = DuckDuckGoSearchTool()
visit_webpage_tool = VisitWebpageTool()

agent = CodeAgent(
    model=model,
    tools=[search_tool, visit_webpage_tool, calculate_cargo_travel_time],
    additional_authorized_imports=["pandas"],
    max_steps=20
)

task = "Find all of the US national parks, calculate the time to transfer via cargo plane from here (we're in Sacramento, CA, 38.581667, -121.494444), and return them to me as a pandas dataframe."

result = agent.run(task)
print(result)

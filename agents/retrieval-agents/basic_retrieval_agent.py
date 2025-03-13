import dotenv
dotenv.load_dotenv()
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

# Initialize the search tool
search_tool = DuckDuckGoSearchTool()

# Initialize the model
model = HfApiModel()

agent = CodeAgent(
    model=model,
    tools=[search_tool]
)

# Example usage
response = agent.run(
    "Search for total body fitness plan ideas, including workouts, diet and mental health."
)
print(response)
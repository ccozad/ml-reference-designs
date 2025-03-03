import dotenv
dotenv.load_dotenv()
from smolagents import CodeAgent, tool, HfApiModel
import yaml
from tools.final_answer import FinalAnswerTool

final_answer = FinalAnswerTool()

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
    custom_role_conversions=None,
)

# Tool to suggest a menu based on the occasion
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion for the party.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal" or occasion == "formal dinner" or occasion == "formal party":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu based on the occasion."

agent = CodeAgent(tools=[final_answer, suggest_menu], model=HfApiModel())

# Preparing the menu for the party
agent.run("Prepare a formal menu for the party.")
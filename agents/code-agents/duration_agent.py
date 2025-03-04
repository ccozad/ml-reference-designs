import dotenv
dotenv.load_dotenv()
from smolagents import CodeAgent, HfApiModel
import yaml
from tools.final_answer import FinalAnswerTool

final_answer = FinalAnswerTool()

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
    custom_role_conversions=None,
)

agent = CodeAgent(
    tools=[final_answer], 
    model=HfApiModel(), 
    additional_authorized_imports=['datetime'])

# Preparing the menu for the party
agent.run(    """
    We need to prepare for a party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """
)
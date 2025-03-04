import dotenv
dotenv.load_dotenv()
from smolagents import CodeAgent, tool, HfApiModel
import yaml
from tools.final_answer import FinalAnswerTool

final_answer = FinalAnswerTool()

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    # it is possible that this model may be overloaded
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
    custom_role_conversions=None,
)

# Estimate one rep max based on the weight and reps
@tool
def estimate_one_rep_max(weight: int, reps: int) -> int:
    """
    Estimates the one rep max based on the weight and reps.
    Args:
        weight: The weight lifted.
        reps: The number of reps performed.
    """
    return int(weight * (1 + reps / 30))

# Tool to suggest a 16 week training plan
@tool
def generate_strength_plan(one_rep_max: int, unit: str) -> str:
    """
    Generates a strength training plan based on the one rep max.
    Args:
        one_rep_max: The one rep max for the strength training plan.
        unit: The unit of measurement for the one rep max such as lbs or kgs.
    """

    workout_plan = f"""
    Here is a 16-week strength training plan based on your one rep max of {one_rep_max} lbs:
    Week 1: 5 sets of 5 reps at 70% of 1RM - {int(one_rep_max * 0.7)} {unit}
    Week 2: 5 sets of 3 reps at 75% of 1RM - {int(one_rep_max * 0.75)} {unit}
    Week 3: 5 sets of 1 rep at 80% of 1RM - {int(one_rep_max * 0.80)} {unit}
    Week 4: Rest and recovery
    Week 5: 5 sets of 5 reps at 75% of 1RM - {int(one_rep_max * 0.75)} {unit}
    Week 6: 5 sets of 3 reps at 80% of 1RM - {int(one_rep_max * 0.80)} {unit}
    Week 7: 5 sets of 1 rep at 85% of 1RM - {int(one_rep_max * 0.85)} {unit}
    Week 8: Rest and recovery
    Week 9: 4 sets of 5 reps at 80% of 1RM - {int(one_rep_max * 0.80)} {unit}
    Week 10: 4 sets of 3 reps at 85% of 1RM - {int(one_rep_max * 0.85)} {unit}
    Week 11: 4 sets of 1 rep at 90% of 1RM - {int(one_rep_max * 0.90)} {unit}
    Week 12: Rest and recovery
    Week 13: 3 sets of 5 reps at 85% of 1RM - {int(one_rep_max * 0.85)} {unit}
    Week 14: 3 sets of 3 reps at 90% of 1RM - {int(one_rep_max * 0.90)} {unit}
    Week 15: 3 sets of 1 rep at 95% of 1RM - {int(one_rep_max * 0.95)} {unit}
    Week 16: Rest and recovery
    Week 17: Test your new 1RM
    """
    
    return workout_plan

agent = CodeAgent(tools=[final_answer, generate_strength_plan, estimate_one_rep_max], model=HfApiModel())

# Prepare a 16 week strength training plan
agent.run("I can deadlift 225 lbs 10 times. Please generate a strength training program for me.")
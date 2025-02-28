import os
import dotenv
dotenv.load_dotenv()
from huggingface_hub import InferenceClient

client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct")

# This model will repeat data over and over because it is called with
# the wrong template.
output = client.text_generation(
    "The capital of france is",
    max_new_tokens=100,
)

print(output)
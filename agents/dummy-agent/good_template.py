import os
import dotenv
dotenv.load_dotenv()
from huggingface_hub import InferenceClient

client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct")

# Unlike the bad template exaple, we'll now se the correct template
# with Llama-3.2-3B-Instruct. This will generate a coherent response.
prompt="""<|begin_of_text|><|start_header_id|>user<|end_header_id|>

The capital of france is<|eot_id|><|start_header_id|>assistant<|end_header_id|>

"""
output = client.text_generation(
    prompt,
    max_new_tokens=100,
)

print(output)
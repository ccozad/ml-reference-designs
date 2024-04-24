import transformers
import torch
import os

from dotenv import load_dotenv
load_dotenv()

model_id = "meta-llama/Meta-Llama-3-8B"

pipeline = transformers.pipeline (
    "text-generation",
    model = model_id,
    model_kwargs = {"torch_dtype": torch.bfloat16},
    device_map="auto",
    token = os.environ.get('HF_AUTH_TOKEN'),
    max_new_tokens = 512
)

result = pipeline("SYSTEM\"\"\"You are cook who knows how to make many types of diner foods. You have been asked to train new cooks by answering their questions. You should break answers into steps.\"\"\"\nQuestion: How do you make a grilled cheese sandwich?\nAnswer: ")
print(result[0]["generated_text"])
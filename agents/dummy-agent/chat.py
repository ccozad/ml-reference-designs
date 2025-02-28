import os
import dotenv
dotenv.load_dotenv()
from huggingface_hub import InferenceClient

client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct")

# Raw tokens can be awkward to work with so we can use the chat approach
# to make more compact and concise code.
output = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "The capital of france is"},
    ],
    stream=False,
    max_tokens=1024,
)

print(output.choices[0].message.content)
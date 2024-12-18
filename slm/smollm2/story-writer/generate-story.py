from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.utils import logging
# Quiet a number of warning emitted by the transformers library
logging.set_verbosity_error()
import random

checkpoint = "HuggingFaceTB/SmolLM2-360M"
#device = "cuda"
device = "cpu" # CPU mode for running on  a Mac Book Pro
tokenizer = AutoTokenizer.from_pretrained(checkpoint, padding_side="left")
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

animals = ["dog", "cat", "bird", "fish", "elephant", "giraffe", "zebra", "lion", "tiger", "bear", "fox"]
first_animal = animals[random.randint(0, len(animals) - 1)]
second_animal = animals[random.randint(0, len(animals) - 1)]

prompt = "Here's a brief children's story about a {0} and a {1} learning about sharing".format(first_animal, second_animal)
inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
# There's large number of tokens in this output so we generate a full story in one shot
# This is fairly slow on a CPU only device. An interactive version should generate less
# tokens to the user and generate the story in multiple steps.
outputs = model.generate(inputs, max_new_tokens=300, do_sample=True, temperature=0.7)

print("SmolLM story writer example:")
print("Story:")
for out in outputs:
    print(tokenizer.decode(out))
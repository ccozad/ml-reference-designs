from transformers import AutoModelForCausalLM, AutoTokenizer
checkpoint = "HuggingFaceTB/SmolLM-360M"
#device = "cuda"
device = "cpu"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

animals = ["dog", "cat", "bird", "fish", "elephant", "giraffe", "zebra", "lion", "tiger", "bear", "fox"]
first_animal = animals[random.randint(0, len(animals) - 1)]
second_animal = animals[random.randint(0, len(animals) - 1)]

prompt = "Write a short children's story about a {0} and a {1}".format(first_animal, second_animal)
inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs)

print("SmolLM story writer example:")
print("Prompt:")
print(prompt)
print("Story:")
print(tokenizer.decode(outputs[0]))
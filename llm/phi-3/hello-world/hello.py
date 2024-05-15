from transformers import AutoModelForCausalLM, AutoTokenizer
# At the time this code was published the Phi-3 model requires
# that remote code execution is enabled to run.
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct", 
    cache_dir="E:/models/",
    trust_remote_code=True)
# At the time this code was published the Phi-3 model requires
# that remote code execution is enabled to run.
tokenizer = AutoTokenizer.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct", 
    cache_dir="E:/models/",
    trust_remote_code=True)

messages = [{"role": "user", "content": "Can you provide a few examples of musical instruments?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

outputs = model.generate(inputs, max_new_tokens=128)
text = tokenizer.batch_decode(outputs)[0]

print("\nMicrosoft Phi-3 LLM Test:\n")
print(text)
import dotenv
dotenv.load_dotenv()

import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="You are a helpful instructor who breaks down complex problems into simple steps.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What are the steps of PEMDAS in math?"
                }
            ]
        }
    ]
)
print(message.content[0].text)
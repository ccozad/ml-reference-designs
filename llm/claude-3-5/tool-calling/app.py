import dotenv
dotenv.load_dotenv()

import random
import json
import anthropic

quotes = json.load(open('quotes.json'))

client = anthropic.Anthropic()
MODEL = "claude-3-5-sonnet-20240620"

tools = [
    {
        "name": "random_quote",
        "description": "A tool that returns a random quote. Returns the quote and author.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]

def process_tool_call(tool_name, tool_input):
    if tool_name == "random_quote":
        return random.choice(quotes)
    else:
        print(f"Unknown tool: {tool_name}")
        return None

def chat_with_claude(user_message):
    print(f"\n{'='*50}\nUser Message: {user_message}\n{'='*50}")

    message = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        messages=[{"role": "user", "content": user_message}],
        tools=tools,
    )

    print(f"\nInitial Response:")
    print(f"Stop Reason: {message.stop_reason}")
    print(f"Content: {message.content}")

    if message.stop_reason == "tool_use":
        tool_use = next(block for block in message.content if block.type == "tool_use")
        tool_name = tool_use.name
        tool_input = tool_use.input

        print(f"\nTool Used: {tool_name}")
        print(f"Tool Input: {tool_input}")

        tool_result = process_tool_call(tool_name, tool_input)

        print(f"Tool Result: {tool_result}")

        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            messages=[
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": message.content},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": str(tool_result),
                        }
                    ],
                },
            ],
            tools=tools,
        )
    else:
        response = message

    final_response = next(
        (block.text for block in response.content if hasattr(block, "text")),
        None,
    )
    print(f"\nFinal Response: {final_response}")

    return final_response

if __name__ == '__main__':
    chat_with_claude("Tell me an inspiring quote.")
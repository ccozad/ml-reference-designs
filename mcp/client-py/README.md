# Introduction

The Model Context Protocol (MCP) is a standards effort by the Anthropic team to create a standardized interface between LLM applications and external data sources. MCP is supported by the Anthropic Desktop client and several other active client projects. The protocol is not specific to any specific LLM and can be used with any LLM that supports tool calling, such as ChatGPT. Additional coding work is required to support other LLMs in the client or server code.

This code is the quick start code for the client, as explained in depth on the MCP website: https://modelcontextprotocol.io/quickstart/server

The client relies on a weather server example explained in the quick start for the server code: https://modelcontextprotocol.io/quickstart/server

The primary difference is this example does not use the `uv` tool, instead it uses the standard tools distributed by python.org.

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Anthropic API key
 - Python virtual environment

**Environment limitation**
There is an unresolved error on Windows at this time. This sample currently only runs on a Mac or Linux.

## Anthropic API key

Create an API key using the Anthropic Dashboard. Copy that key for use in the next step. Create a file named `.env` in the folder where this `README.md` file resides.

Add the following line to your environment file:

```ini
ANTHROPIC_API_KEY=<your key>
```

## Python Virtual Environment

 - Move to the mcp/client-py folder
   - `cd <mcp/client-py>`
 - Create a virtual environment
   - On Mac: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - Activate the virtual environment
   - On Mac: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
 - Install dependencies
   - On Mac: `pip3 install -r requirements.txt`
   - On Windows: `pip install -r requirements.txt`
 - Call a specific script
   - On Mac: `python3 <script_name>.py`
   - On Windows: `python <script_name>.py`
 - Deactivate virtual environment
   - `deactivate`

# Running the code

`python3 client.py <path to mcp server>`

# Example output (short)

The output with just the conversation between the user and the LLM

```
.venv) client-py % python3 client.py ../weather-server-py/src/weather/server.py

Connected to server with tools: ['get-alerts', 'get-forecast']

MCP Client Started!
Type your queries or 'quit' to exit.

Query: What is the weather in Sacramento?

[Text response from Claude]: 
Let me get the weather forecast for Sacramento, CA. Sacramento's coordinates are approximately 38.5816° N, 121.4944° W.

[Tool use response from Claude]: get-forecast {'latitude': 38.5816, 'longitude': -121.4944}

[Calling tool get-forecast with args {'latitude': 38.5816, 'longitude': -121.4944}]

[Response from Claude]:
Currently in Sacramento, you can expect the following weather tonight:
- Temperature: 52°F
- Wind: 6 mph from the SSE (South-Southeast)
- Conditions: Slight chance of rain showers followed by patchy fog

Looking ahead to tomorrow (Saturday):
- Temperature: 60°F
- Wind: 7 mph SSE
- Conditions: Patchy fog

There's rain in the forecast for the weekend, with showers expected Saturday night and Sunday, before clearing up to sunny conditions by Monday.

Query: quit
```

# Example output (full)

The full output with debug messages

```text
(.venv) client-py % python3 client.py ../weather-server-py/src/weather/server.py

Connected to server with tools: ['get-alerts', 'get-forecast']

MCP Client Started!
Type your queries or 'quit' to exit.

Query: What is the weather in Sacramento?

[Calling Claude with query]: What is the weather in Sacramento?

Available tools: [{'name': 'get-alerts', 'description': 'Get weather alerts for a state', 'input_schema': {'type': 'object', 'properties': {'state': {'type': 'string', 'description': 'Two-letter state code (e.g. CA, NY)'}}, 'required': ['state']}}, {'name': 'get-forecast', 'description': 'Get weather forecast for a location', 'input_schema': {'type': 'object', 'properties': {'latitude': {'type': 'number', 'description': 'Latitude of the location'}, 'longitude': {'type': 'number', 'description': 'Longitude of the location'}}, 'required': ['latitude', 'longitude']}}]

[Text response from Claude]: Let me get the weather forecast for Sacramento, CA. Sacramento's coordinates are approximately 38.5816° N, 121.4944° W.

[Tool use response from Claude]: get-forecast {'latitude': 38.5816, 'longitude': -121.4944}

[Calling tool get-forecast with args {'latitude': 38.5816, 'longitude': -121.4944}]

[Tool result]: [TextContent(type='text', text="Forecast for 38.5816, -121.4944:\n\nTonight:\nTemperature: 52°F\nWind: 6 mph SSE\nSlight Chance Rain Showers then Patchy Fog\n---\nSaturday:\nTemperature: 60°F\nWind: 7 mph SSE\nPatchy Fog\n---\nSaturday Night:\nTemperature: 52°F\nWind: 5 to 12 mph S\nRain Showers\n---\nSunday:\nTemperature: 59°F\nWind: 7 to 15 mph S\nRain Showers\n---\nSunday Night:\nTemperature: 41°F\nWind: 2 to 7 mph SW\nSlight Chance Rain Showers then Partly Cloudy\n---\nMonday:\nTemperature: 55°F\nWind: 5 to 8 mph NNW\nSunny\n---\nMonday Night:\nTemperature: 38°F\nWind: 6 mph NNW\nMostly Clear\n---\nTuesday:\nTemperature: 54°F\nWind: 5 mph NNW\nMostly Sunny\n---\nTuesday Night:\nTemperature: 37°F\nWind: 3 mph NNE\nPartly Cloudy\n---\nNew Year's Day:\nTemperature: 54°F\nWind: 3 mph N\nPartly Sunny\n---\nWednesday Night:\nTemperature: 40°F\nWind: 2 mph N\nMostly Cloudy\n---\nThursday:\nTemperature: 56°F\nWind: 3 mph NNE\nPartly Sunny\n---\nThursday Night:\nTemperature: 42°F\nWind: 2 mph ESE\nMostly Cloudy\n---\nFriday:\nTemperature: 57°F\nWind: 3 mph SSE\nMostly Cloudy then Slight Chance Rain Showers\n---")]

[Response from Claude]: Currently in Sacramento, you can expect the following weather tonight:
- Temperature: 52°F
- Wind: 6 mph from the SSE (South-Southeast)
- Conditions: Slight chance of rain showers followed by patchy fog

Looking ahead to tomorrow (Saturday):
- Temperature: 60°F
- Wind: 7 mph SSE
- Conditions: Patchy fog

There's rain in the forecast for the weekend, with showers expected Saturday night and Sunday, before clearing up to sunny conditions by Monday.

Final text: ["Let me get the weather forecast for Sacramento, CA. Sacramento's coordinates are approximately 38.5816° N, 121.4944° W.", "[Calling tool get-forecast with args {'latitude': 38.5816, 'longitude': -121.4944}]", "Currently in Sacramento, you can expect the following weather tonight:\n- Temperature: 52°F\n- Wind: 6 mph from the SSE (South-Southeast)\n- Conditions: Slight chance of rain showers followed by patchy fog\n\nLooking ahead to tomorrow (Saturday):\n- Temperature: 60°F\n- Wind: 7 mph SSE\n- Conditions: Patchy fog\n\nThere's rain in the forecast for the weekend, with showers expected Saturday night and Sunday, before clearing up to sunny conditions by Monday."]

Let me get the weather forecast for Sacramento, CA. Sacramento's coordinates are approximately 38.5816° N, 121.4944° W.
[Calling tool get-forecast with args {'latitude': 38.5816, 'longitude': -121.4944}]
Currently in Sacramento, you can expect the following weather tonight:
- Temperature: 52°F
- Wind: 6 mph from the SSE (South-Southeast)
- Conditions: Slight chance of rain showers followed by patchy fog

Looking ahead to tomorrow (Saturday):
- Temperature: 60°F
- Wind: 7 mph SSE
- Conditions: Patchy fog

There's rain in the forecast for the weekend, with showers expected Saturday night and Sunday, before clearing up to sunny conditions by Monday.

Query: quit
(.venv) client-py % 
```
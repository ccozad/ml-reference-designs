# Overview

Based on a voice agent cookbook recipe by OpenAI https://cookbook.openai.com/examples/agents_sdk/app_assistant_voice_agents

# Dependencies

You will need all of the following dependencies to run this example:

 - OpenAI API key
 - Python virtual environment
 - Download example knowledge data
 - Vector store

## OpenAI API token

Log in to OpenAI and retrieve your API key

Create an environment file named `.env`. Add the following line to your environment file:

```ini
OPENAI_API_KEY=<your token>
```

## Python Virtual Environment

 - Move to the multi-agents folder
   - `cd <agents/audio-agent>`
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

## Download example knowledge data

 - Create a folder named `voice_agents_knowledge` 
 - Visit https://github.com/openai/openai-cookbook/tree/main/examples/agents_sdk/voice_agents_knowledge
 - Download the product catalog pdf to `voice_agents_knowledge` 

## Vector store

Run `python init_vector_db.py` which will print out a vector store ID. Add this ID to the config file.

```ini
VECTOR_STORE_ID=<id>
```

# Running the Code

```
python text_app.py
User: What's my ACME account balance doc? My user ID is 1234567890
Your account balance is £72.50. You have a Gold Executive membership.
---
User: Ooh i've got money to spend! How big is the input and how fast is the output of the dynamite dispenser?
The Automated Dynamite Dispenser has a capacity to hold 10 sticks of dynamite, and it dispenses at a speed of 1 stick every 2 seconds.
---
User: Hmmm, what about duck hunting gear - what's trending right now?
Staying updated with the latest advancements in duck hunting gear can significantly enhance your hunting experience. Here are some trending items for 2025:



**Sitka Delta Zip Waders**
These waders feature reinforced shins and knees with rugged foam pads, providing durability for challenging terrains. The GORE-TEX material ensures you stay dry throughout the season. ([blog.gritroutdoors.com](https://blog.gritroutdoors.com/must-have-duck-hunting-gear-for-a-winning-season/?utm_source=openai))

**Banded Aspire Catalyst Waders**
Designed for all-season use, these waders incorporate waterproof-breathable technology for comfort in various conditions. They include PrimaLoft Aerogel insulation for thermal protection and an integrated LED light in the chest pocket for added convenience. ([blog.gritroutdoors.com](https://blog.gritroutdoors.com/must-have-duck-hunting-gear-for-a-winning-season/?utm_source=openai))

**Avian-X A-Frame Blind**
This mobile hunting blind offers a non-corrosive aluminum frame and a 600 denier shell, providing durability and protection against wind and rain. Its Mossy Oak Shadowgrass camouflage ensures effective concealment in diverse environments. ([gunnewsdaily.com](https://gunnewsdaily.com/best-new-duck-hunting-accessories/?utm_source=openai))

**MOJO Motion Decoys**
These decoys utilize motion to mimic real waterfowl behavior, effectively attracting ducks from a distance. Their realistic movement adds authenticity to your decoy spread. ([media.lalafurn.com](https://media.lalafurn.com/how-advancements-in-technology-are-shaping-the-future-of-duck-hunting/?utm_source=openai))

**Sitka Full Choke Pack**
This backpack-style blind bag offers comfort and efficiency, featuring durable zippers and straps. It provides ample space for gear, keeping items dry even in harsh conditions. ([bornhunting.com](https://bornhunting.com/top-duck-hunting-gear/?utm_source=openai))

Incorporating these items into your gear can enhance your comfort, efficiency, and success during the hunting season.
---
```
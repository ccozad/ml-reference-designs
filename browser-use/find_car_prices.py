from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Use autotrader.com to find car prices for a make of toyota and model of corolla in the 95621 zip code. Stop when you have gathered 5 prices and present a summary." ,
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())
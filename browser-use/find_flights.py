from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

provider = "https://www.united.com/en/us/"
departure_date = "May 30"
origin = "SMF"
destination = "LAX"
seat_class = "Economy"
max_price = 2000

prompt = """
You are a travel assistant responsible for booking flights.

Use the site {provider} to find flights with the following criteria:

Use the following search criteria:
- One way
- Departure date: {departure_date}
- Leaving from: {origin}
- Going to: {destination}
- Seat class: {seat_class}

Selection criteria:
- Sort by price and show the cheapest options first.
- No more than one stop
- Cost should not exceed {max_price}

If you find a flight that meets the criteria, select it and pick the cheapest price.

Stop before going to the checkout. Print the airline, price and flight number in the final response.
""".format(
    provider=provider,
    departure_date=departure_date,
    origin=origin,
    destination=destination,
    max_price=max_price,
    seat_class=seat_class,
)

async def main():
    agent = Agent(
        task=prompt,
        llm=ChatOpenAI(model="gpt-4o"),
        planner_llm=ChatOpenAI(model="o3-mini"),
        use_vision_for_planner=False,
        planner_interval=4
    )
    await agent.run()

asyncio.run(main())
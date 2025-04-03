# Introduction

This example shows how an assistant can be used to make travel arrangement. The work is based on a detailed tutorial by LangGraph https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/ 

 - The zero-shot agent represents how a fully automated workflow might go. The agent may take expensive actions like booking a flight without user approval.
 - The confirmation agent asks the user if it is ok to proceed before each action. This agent asks for confirmation after EVERY action, even non destructive actions
 - The smart confirm agent only asks for confirmation on actions that write to the database.

# Dependencies

You will need all of the following dependencies to run this example:

 - API Keys
   - Anthropic
   - OpenAI
 - Python virtual environment

## API Keys

Create an environment file named `.env`. Add the following content to your environment file.

```ini
ANTHROPIC_API_KEY=<your key>
OPENAI_API_KEY=<your key>
```

## Python Virtual Environment

 - Move to the workout-agents folder
   - `cd <lang-graph/travel-agent>`
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

## Zero shot agent

Run the command `python zero_shot_agent.py`


``` text
python zero_shot_agent.py

1. Initializing the database...
 - Database exists locally.
2. Initializing the LLM...
 - LLM initialized.
3. Initializing the assistant...
4. Running the assistant...
================================ Human Message =================================

Hi there, what time is my flight?
================================== Ai Message ==================================

[{'text': 'Okay, let me look up your flight details using the `fetch_user_flight_information` tool.', 'type': 'text'}, {'id': 'toolu_01F5WhRQ9nPuS8VtT8BS3Pha', 'input': {}, 'name': 'fetch_user_flight_information', 'type': 'tool_use'}]
Tool Calls:
  fetch_user_flight_information (toolu_01F5WhRQ9nPuS8VtT8BS3Pha)
 Call ID: toolu_01F5WhRQ9nPuS8VtT8BS3Pha
  Args:
================================= Tool Message =================================
Name: fetch_user_flight_information

[{"ticket_no": "7240005432906569", "book_ref": "C46E9F", "flight_id": 19250, "flight_no": "LX0112", "departure_airport": "CDG", "arrival_airport": "BSL", "scheduled_departure": "2025-04-02 22:56:02.744230-04:00", "scheduled_arrival": "2025-04-03 00:26:02.744230-04:00", "seat_no": "18E", "fare_conditions": "Economy"}]
================================== Ai Message ==================================

Based on the flight information fetched, your flight LX0112 from Paris (CDG) to Basel (BSL) is scheduled to depart at 10:56 PM on April 2nd, 2025 and arrive at 12:26 AM on April 3rd, 2025. Your seat assignment is 18E in the economy class cabin.

Please let me know if you need any other details about your flight!
================================ Human Message =================================

Am I allowed to update my flight to something sooner? I want to leave later today.
================================== Ai Message ==================================

[{'text': "To check if you're allowed to update your flight, let me consult the company policies first using the `lookup_policy` tool.", 'type': 'text'}, {'id': 'toolu_01PChzUo34sUjZ5m6ch32aSW', 'input': {'query': 'flight change policy'}, 'name': 'lookup_policy', 'type': 'tool_use'}]
Tool Calls:
  lookup_policy (toolu_01PChzUo34sUjZ5m6ch32aSW)
 Call ID: toolu_01PChzUo34sUjZ5m6ch32aSW
  Args:
    query: flight change policy
================================= Tool Message =================================
Name: lookup_policy


## Booking and Cancellation

1. How can I change my booking?
        * The ticket number must start with 724 (SWISS ticket no./plate).
        * The ticket was not paid for by barter or voucher (there are exceptions to voucher payments; if the ticket was paid for in full by voucher, then it may be possible to rebook online under certain circumstances. If it is not possible to rebook online because of the payment method, then you will be informed accordingly during the rebooking process).
        * There must be an active flight booking for your ticket. It is not possible to rebook open tickets or tickets without the corresponding flight segments online at the moment.
        * It is currently only possible to rebook outbound (one-way) tickets or return tickets with single flight routes (point-to-point).
2. Which tickets/bookings cannot be rebooked online currently?
        * Bookings containing flight segments with other airlines
        * Bookings containing reservations, where a ticket has not yet been issued
        * Bookings with several valid tickets for the same person and route
        * Tickets with a status other than O (open) (A)
        * Bookings with segments with a status other than OK (e.g. containing flight segments with the status Waitlist) (HK|RR)
        * Tickets that do not display the tariff calculation (IT tickets)
        * Bookings that contain special services (e.g. transportation of animals/transportation of medica ... (truncated)
================================== Ai Message ==================================

[{'text': "Based on the policy details, it seems you are allowed to update or change your flight as long as your ticket number starts with 724 (indicating it's a SWISS ticket), the ticket was not paid with a voucher or barter, and there is an active flight booking associated with the ticket.\n\nThe policy mentions that you can change the flight and travel dates online, but not the origin/destination or passenger name. There may be a fee for changing to a different flight depending on your fare conditions.\n\nTo proceed with updating to an earlier flight today, let me first search for available flights using the `search_flights` tool:", 'type': 'text'}, {'id': 'toolu_01FdM8WonrgbnmjkDb6btR9c', 'input': {'departure_airport': 'CDG', 'arrival_airport': 'BSL', 'start_time': '2025-04-02T00:00:00', 'end_time': '2025-04-02T23:59:59'}, 'name': 'search_flights', 'type': 'tool_use'}]
Tool Calls:
  search_flights (toolu_01FdM8WonrgbnmjkDb6btR9c)
 Call ID: toolu_01FdM8WonrgbnmjkDb6btR9c
  Args:
    departure_airport: CDG
    arrival_airport: BSL
    start_time: 2025-04-02T00:00:00
    end_time: 2025-04-02T23:59:59
================================= Tool Message =================================
Name: search_flights

[{"flight_id": 19250, "flight_no": "LX0112", "scheduled_departure": "2025-04-02 22:56:02.744230-04:00", "scheduled_arrival": "2025-04-03 00:26:02.744230-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "On Time", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}]
================================== Ai Message ==================================

[{'text': 'The search shows that your currently booked flight LX0112 at 10:56 PM is the only available option for today from Paris to Basel.\n\nLet me try broadening the search to include surrounding airports as well:', 'type': 'text'}, {'id': 'toolu_01XN86B2eurBftCrfhxXy9of', 'input': {'start_time': '2025-04-02T00:00:00', 'end_time': '2025-04-02T23:59:59'}, 'name': 'search_flights', 'type': 'tool_use'}]
Tool Calls:
  search_flights (toolu_01XN86B2eurBftCrfhxXy9of)
 Call ID: toolu_01XN86B2eurBftCrfhxXy9of
  Args:
    start_time: 2025-04-02T00:00:00
    end_time: 2025-04-02T23:59:59
================================= Tool Message =================================
Name: search_flights

[{"flight_id": 46, "flight_no": "DL0042", "scheduled_departure": "2025-04-02 14:31:02.744230-04:00", "scheduled_arrival": "2025-04-02 15:26:02.744230-04:00", "departure_airport": "BSL", "arrival_airport": "HAM", "status": "Arrived", "aircraft_code": "321", "actual_departure": "2025-04-02 14:34:02.744230-04:00", "actual_arrival": "2025-04-02 15:29:02.744230-04:00"}, {"flight_id": 48, "flight_no": "DL0066", "scheduled_departure": "2025-04-02 16:21:02.744230-04:00", "scheduled_arrival": "2025-04-02 17:16:02.744230-04:00", "departure_airport": "BSL", "arrival_airport": "HAM", "status": "Arrived", "aircraft_code": "321", "actual_departure": "2025-04-02 16:26:02.744230-04:00", "actual_arrival": "2025-04-02 17:21:02.744230-04:00"}, {"flight_id": 49, "flight_no": "EK0005", "scheduled_departure": "2025-04-02 17:21:02.744230-04:00", "scheduled_arrival": "2025-04-02 18:16:02.744230-04:00", "departure_airport": "BSL", "arrival_airport": "HAM", "status": "Arrived", "aircraft_code": "321", "actual_departure": "2025-04-02 17:24:02.744230-04:00", "actual_arrival": "2025-04-02 18:20:02.744230-04:00"}, {"flight_id": 92, "flight_no": "UA0047", "scheduled_departure": "2025-04-02 00:01:02.744230-04:00", "scheduled_arrival": "2025-04-02 00:56:02.744230-04:00", "departure_airport": "BSL", "arrival_airport": "HAM", "status": "Arrived", "aircraft_code": "321", "actual_departure": "2025-04-02 ... (truncated)
================================== Ai Message ==================================

Unfortunately, even after expanding the search, there are no earlier SWISS flights available from Paris CDG to Basel BSL on your travel date of April 2nd, 2025.

The policy states that you can change your flight dates online, but cannot change the origin/destination airports. So if you wanted to fly out earlier today, you'd likely need to book a completely new one-way ticket, which may not be ideal.

Let me know if you'd still like me to try changing your existing ticket to the 10:56 PM LX0112 flight using the `update_ticket_to_new_flight` tool, or if you'd prefer to keep your original schedule.
================================ Human Message =================================

Update my flight to sometime next week then
================================== Ai Message ==================================

[{'text': "Okay, let's try updating your flight to sometime next week instead. I'll search for available SWISS flights from Paris (CDG) to Basel (BSL) between April 6th and April 12th.", 'type': 'text'}, {'id': 'toolu_01BNSYTCgrnCN8o6kXDN5JfJ', 'input': {'departure_airport': 'CDG', 'arrival_airport': 'BSL', 'start_time': '2025-04-06', 'end_time': '2025-04-12'}, 'name': 'search_flights', 'type': 'tool_use'}]
Tool Calls:
  search_flights (toolu_01BNSYTCgrnCN8o6kXDN5JfJ)
 Call ID: toolu_01BNSYTCgrnCN8o6kXDN5JfJ
  Args:
    departure_airport: CDG
    arrival_airport: BSL
    start_time: 2025-04-06
    end_time: 2025-04-12
================================= Tool Message =================================
Name: search_flights

[{"flight_id": 19232, "flight_no": "LX0112", "scheduled_departure": "2025-04-06 22:56:02.744230-04:00", "scheduled_arrival": "2025-04-07 00:26:02.744230-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19238, "flight_no": "LX0112", "scheduled_departure": "2025-04-10 22:56:02.744230-04:00", "scheduled_arrival": "2025-04-11 00:26:02.744230-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19242, "flight_no": "LX0112", "scheduled_departure": "2025-04-11 22:56:02.744230-04:00", "scheduled_arrival": "2025-04-12 00:26:02.744230-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19251, "flight_no": "LX0112", "scheduled_departure": "2025-04-09 22:56:02.744230-04:00", "scheduled_arrival": "2025-04-10 00:26:02.744230-04:00", "departure_airport": "CDG", "arrival_airport": "BSL", "status": "Scheduled", "aircraft_code": "SU9", "actual_departure": null, "actual_arrival": null}, {"flight_id": 19252, "flight_no": "LX0112", "scheduled_departure": "2025-04-08 22:56:02.744230-04:00", "scheduled_arrival": "2025-04-09 00:2 ... (truncated)
================================== Ai Message ==================================

The search shows there is one SWISS flight (LX0112) available daily from Paris CDG to Basel BSL next week, with a departure time of 10:56 PM each night.

Which day would you prefer me to update your ticket to? I'll need your original ticket number starting with 7240005432906569 to proceed with the change using the `update_ticket_to_new_flight` tool.
================================ Human Message =================================

The next available option is great
================================== Ai Message ==================================

[{'text': 'Got it, let me update your ticket to the next available SWISS flight LX0112 from Paris (CDG) to Basel (BSL) using the `update_ticket_to_new_flight` tool:', 'type': 'text'}, {'id': 'toolu_01TAv2y8RrVKw7eKKUZDnKZh', 'input': {'ticket_no': '7240005432906569', 'new_flight_id': 19232}, 'name': 'update_ticket_to_new_flight', 'type': 'tool_use'}]
Tool Calls:
  update_ticket_to_new_flight (toolu_01TAv2y8RrVKw7eKKUZDnKZh)
 Call ID: toolu_01TAv2y8RrVKw7eKKUZDnKZh
  Args:
    ticket_no: 7240005432906569
    new_flight_id: 19232
================================= Tool Message =================================
Name: update_ticket_to_new_flight

Ticket successfully updated to new flight.
================================== Ai Message ==================================

Your ticket number 7240005432906569 has been successfully updated to the new flight:

Flight: LX0112
Date: April 6th, 2025  
Departure: Paris (CDG) at 10:56 PM
Arrival: Basel (BSL) at 12:26 AM (April 7th)

Your seat assignment of 18E in economy class remains the same. Please let me know if you need any other details about your updated flight itinerary.

Since this was just a change of flight date/time and not a new booking, your ticket number will stay the same as before. Feel free to check your updated flight details online as well using this ticket number.

Travel safely and have a great trip!
```

## Confirmation agent

Run the command `python confirmation agent`

```text
python confirmation_agent.py

1. Initializing the database...
 - Database exists locally.
2. Initializing the LLM...
 - LLM initialized.
3. Initializing the assistant...
4. Running the assistant...
================================ Human Message =================================

Hi there, what time is my flight?
================================== Ai Message ==================================

[{'text': "To check the details of your upcoming flight, I'll need to fetch your ticket information first. Let me invoke the tool to retrieve your tickets and associated flight details:", 'type': 'text'}, {'id': 'toolu_01GZPoqPT1BQjx4HBu8VHB24', 'input': {}, 'name': 'fetch_user_flight_information', 'type': 'tool_use'}]
Tool Calls:
  fetch_user_flight_information (toolu_01GZPoqPT1BQjx4HBu8VHB24)
 Call ID: toolu_01GZPoqPT1BQjx4HBu8VHB24
  Args:
Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested change.

y
================================ Human Message =================================

Am I allowed to update my flight to something sooner? I want to leave later today.
================================== Ai Message ==================================

[{'text': 'Okay, let me first check the company policies to see if updating flights on short notice is permitted:', 'type': 'text'}, {'id': 'toolu_01PN4jBY2HWaTHxHNX1Rj5bQ', 'input': {'query': 'updating flights on short notice'}, 'name': 'lookup_policy', 'type': 'tool_use'}]
Tool Calls:
  lookup_policy (toolu_01PN4jBY2HWaTHxHNX1Rj5bQ)
 Call ID: toolu_01PN4jBY2HWaTHxHNX1Rj5bQ
  Args:
    query: updating flights on short notice
Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested change.

y
================================ Human Message =================================

Update my flight to sometime next week then
================================== Ai Message ==================================

[{'text': 'Okay, let me search for available flights for you next week instead:', 'type': 'text'}, {'id': 'toolu_014Z8LmfvQR43mfJMBMP9vfd', 'input': {'start_time': '2025-04-07', 'end_time': '2025-04-14'}, 'name': 'search_flights', 'type': 'tool_use'}]
Tool Calls:
  search_flights (toolu_014Z8LmfvQR43mfJMBMP9vfd)
 Call ID: toolu_014Z8LmfvQR43mfJMBMP9vfd
  Args:
    start_time: 2025-04-07
    end_time: 2025-04-14
Do you approve of the above actions? Type 'y' to continue; otherwise, explain your requested change.

no, I changed my mind
================================ Human Message =================================

That's all for today, thanks!
================================== Ai Message ==================================

You're welcome! Thank you for reaching out to Swiss Airlines. I'm glad I could provide some information about our policies for updating and canceling flights, even though we didn't end up needing to make any changes this time. Feel free to contact us again whenever you need assistance with booking, changing reservations, or have any other questions. We're always happy to help make your travel experience smooth and enjoyable. Have a great rest of your day!
```
# Introduction

Browser Use is a YCombinator backed startup with an open source library that can control a browser window using Playright and an agentic AI controlled by a language model.

https://github.com/browser-use/browser-use

[![Browser Use Demo - Gather Car Prices](https://img.youtube.com/vi/rDLlWlCFW6A/0.jpg)](https://www.youtube.com/watch?v=rDLlWlCFW6A)

# Dependencies

You will need all of the following dependencies to run this example:

 - OpenAI API token
 - Python virtual environment
 - Install Chromium plugin for Playwright

## OpenAI API token

Log in to OpenAI and retrieve your API token

Create an environment file named `.env`. Add the following line to your environment file:

```ini
OPENAI_API_KEY=<your token>
```

## Python Virtual Environment

 - Move to the multi-agents folder
   - `cd <browser-use>`
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

## Install Chromium plugin for Playwright

Playright was installed with the requirements.txt file.

Run the command `playwright install chromium` to install the plugin used to control the browser.

# Run the code

## Find Car Prices

Run the code using the command `python find_car_prices.py`

```text
python find_car_prices.py
INFO     [browser_use] BrowserUse logging setup complete with level info
INFO     [root] Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.
  value['message'] = load(value['message'])
INFO     [agent] 🚀 Starting task: Use autotrader.com to find car prices for a make of toyota and model of corolla in the 95621 zip code. Stop when you have gathered 5 prices and present a summary.
INFO     [agent] 📍 Step 1
INFO     [agent] 🤷 Eval: Unknown - I just started the task and I am on a blank page.
INFO     [agent] 🧠 Memory: Starting the task to find 5 car prices for Toyota Corolla in the 95621 zip code on autotrader.com.
INFO     [agent] 🎯 Next goal: Open autotrader.com in a new tab to begin the search.   
INFO     [agent] 🛠️  Action 1/1: {"open_tab":{"url":"https://www.autotrader.com"}}     
INFO     [controller] 🔗  Opened new tab with https://www.autotrader.com
INFO     [agent] 📍 Step 2
INFO     [agent] 👍 Eval: Success - Opened Autotrader and found the search options.
INFO     [agent] 🧠 Memory: On Autotrader homepage. Ready to search for Toyota Corolla in 95621 ZIP code. 0 out of 5 prices gathered.
INFO     [agent] 🎯 Next goal: Select 'Toyota' for the make and 'Corolla' for the model, then enter the ZIP code '95621'.
INFO     [agent] 🛠️  Action 1/4: {"select_dropdown_option":{"index":7,"text":"Toyota"} 
}
INFO     [agent] 🛠️  Action 2/4: {"select_dropdown_option":{"index":8,"text":"Corolla" 
}}
INFO     [agent] 🛠️  Action 3/4: {"input_text":{"index":9,"text":"95621"}}
INFO     [agent] 🛠️  Action 4/4: {"click_element":{"index":10}}
INFO     [controller] selected option Toyota with value ['TOYOTA'] in frame 0
INFO     [controller] selected option Corolla with value ['COROL'] in frame 0
INFO     [controller] ⌨️  Input 95621 into index 9
INFO     [controller] 🖱️  Clicked button with index 10: Search
INFO     [agent] 📍 Step 3
INFO     [agent] ⚠ Eval: Failed - The page did not load correctly and it's blank.
INFO     [agent] 🧠 Memory: Search page loaded incorrectly; no interactive elements found. 0 out of 5 prices gathered.
INFO     [agent] 🎯 Next goal: Refresh the page to try loading the content again.      
INFO     [agent] 🛠️  Action 1/2: {"wait":{"seconds":3}}
INFO     [agent] 🛠️  Action 2/2: {"go_to_url":{"url":"https://www.autotrader.com/cars- 
for-sale/all-cars/toyota/corolla/citrus-heights-ca?zip=95621"}}
INFO     [controller] 🕒  Waiting for 3 seconds
INFO     [controller] 🔗  Navigated to https://www.autotrader.com/cars-for-sale/all-cars/toyota/corolla/citrus-heights-ca?zip=95621
INFO     [agent] 📍 Step 4
INFO     [agent] 👍 Eval: Success - Page loaded with search results and pricing information visible.
INFO     [agent] 🧠 Memory: On the results page for Toyota Corolla in 95621. 0 out of 5 prices gathered yet.
INFO     [agent] 🎯 Next goal: Scroll down to gather the first five car prices for Toyota Corolla.
INFO     [agent] 🛠️  Action 1/2: {"scroll_down":{}}
INFO     [agent] 🛠️  Action 2/2: {"extract_content":{"goal":"Find and extract the pric 
es of five Toyota Corolla cars."}}
INFO     [controller] 🔍  Scrolled down the page by one page
INFO     [controller] 📄  Extracted from page
: ```json
{
    "Toyota Corolla Prices": [
        {
            "model": "Certified 2021 Toyota Corolla LE",
            "price": 17699
        },
        {
            "model": "Used 2019 Toyota Corolla SE",
            "price": 15549
        },
        {
            "model": "Certified 2024 Toyota Corolla LE",
            "price": 24900
        },
        {
            "model": "Used 2015 Toyota Corolla L",
            "price": 14488
        },
        {
            "model": "Used 2022 Toyota Corolla LE",
            "price": 22899
        }
    ]
}
```

INFO     [agent] 📍 Step 5
INFO     [agent] 👍 Eval: Success - Five car prices were extracted successfully.
INFO     [agent] 🧠 Memory: Extracted 5 prices. Task completed successfully.
INFO     [agent] 🎯 Next goal: Summarize and complete the task.
INFO     [agent] 🛠️  Action 1/1: {"done":{"text":"Found 5 prices for Toyota Corolla in 
 ZIP 95621: \n\n1. Certified 2021 Toyota Corolla LE - $17,699\n2. Used 2019 Toyota Corolla SE - $15,549\n3. Certified 2024 Toyota Corolla LE - $24,900\n4. Used 2015 Toyota Corolla L - $14,488\n5. Used 2022 Toyota Corolla LE - $22,899","success":true}}
INFO     [agent] 📄 Result: Found 5 prices for Toyota Corolla in ZIP 95621:

1. Certified 2021 Toyota Corolla LE - $17,699
2. Used 2019 Toyota Corolla SE - $15,549
3. Certified 2024 Toyota Corolla LE - $24,900
4. Used 2015 Toyota Corolla L - $14,488
5. Used 2022 Toyota Corolla LE - $22,899
INFO     [agent] ✅ Task completed
INFO     [agent] ✅ Successfully
```
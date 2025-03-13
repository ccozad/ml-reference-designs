# Dependencies

You will need all of the following dependencies to run this example:

 - Hugging Face token
 - Python virtual environment

## Hugging Face token

Log in to Hugging Face and retrieve your token from https://hf.co/settings/tokens

Create an environment file named `.env`. Add the following line to your environment file:

```ini
HF_TOKEN=<your token>
```

## Python Virtual Environment

 - Move to the hello world folder
   - `cd <agents/workout-agents>`
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

## Strength training plan agent

Run the command `python strength_plan_agent.py` to generate a strength training program based on number of reps for a given weight.

```text
python strength_plan_agent.py
╭────────────────────────────────────────────────── New run ──────────────────────────────────────────────────╮
│                                                                                                             │
│ I can deadlift 225 lbs 10 times. Please generate a strength training program for me.                        │
│                                                                                                             │
╰─ HfApiModel - Qwen/Qwen2.5-Coder-32B-Instruct ──────────────────────────────────────────────────────────────╯
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing parsed code: ──────────────────────────────────────────────────────────────────────────────────── 
  one_rep_max = estimate_one_rep_max(weight=225, reps=10)                                                      
  print("Estimated 1RM:", one_rep_max)                                                                         
 ───────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Execution logs:
Estimated 1RM: 300

Out: None
[Step 0: Duration 4.15 seconds| Input tokens: 2,188 | Output tokens: 77]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 2 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing parsed code: ──────────────────────────────────────────────────────────────────────────────────── 
  strength_plan = generate_strength_plan(one_rep_max=300, unit="lbs")                                          
  final_answer(strength_plan)                                                                                  
 ───────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Out - Final answer: 
    Here is a 16-week strength training plan based on your one rep max of 300 lbs:
    Week 1: 5 sets of 5 reps at 70% of 1RM - 210 lbs
    Week 2: 5 sets of 3 reps at 75% of 1RM - 225 lbs
    Week 3: 5 sets of 1 rep at 80% of 1RM - 240 lbs
    Week 4: Rest and recovery
    Week 5: 5 sets of 5 reps at 75% of 1RM - 225 lbs
    Week 6: 5 sets of 3 reps at 80% of 1RM - 240 lbs
    Week 7: 5 sets of 1 rep at 85% of 1RM - 255 lbs
    Week 8: Rest and recovery
    Week 9: 4 sets of 5 reps at 80% of 1RM - 240 lbs
    Week 10: 4 sets of 3 reps at 85% of 1RM - 255 lbs
    Week 11: 4 sets of 1 rep at 90% of 1RM - 270 lbs
    Week 12: Rest and recovery
    Week 13: 3 sets of 5 reps at 85% of 1RM - 255 lbs
    Week 14: 3 sets of 3 reps at 90% of 1RM - 270 lbs
    Week 15: 3 sets of 1 rep at 95% of 1RM - 285 lbs
    Week 16: Rest and recovery
    Week 17: Test your new 1RM
    
[Step 1: Duration 3.11 seconds| Input tokens: 4,559 | Output tokens: 140]

(.venv) D:\Github\ml-reference-designs\agents\workout-agents>
```
import google.generativeai as genai
from config import GEMINI_API_KEY
import json
import re

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')


def generate_plan(user_prompt: str) -> list:
    """
    Uses the Gemini API to generate a structured plan from a user prompt.
    """
    print("🤖 PLANNER: Thinking... Contacting Gemini API...")

    # We have expanded the instructions to include all our agents' skills.
    instruction_prompt = f"""
    You are the planner for a multi-agent AI system. Your job is to analyze a user's request and create a step-by-step plan.
    
    The user's request is: "{user_prompt}"

    Here are the available tools:
    # Wedding Planning Tools
    - agent: "assistant_emma", task: "find_available_venues", params: {{{{ "max_price": "<budget in numbers>" }}}}
    - agent: "style_guru_maya", task: "get_moodboard", params: {{{{ "style": "<style>" }}}}
    
    # --- NEW TOOLS ADDED ---
    # Fitness & Finance Tools
    - agent: "fitcoach_alex", task: "book_gym_class", params: {{{{ "class_name": "Weekly HIIT Session", "date": "Next Monday" }}}}
    - agent: "money_maven_sarah", task: "setup_auto_transfer", params: {{{{ "amount": "<calculated weekly amount>", "frequency": "weekly" }}}}
    
    Analyze the user's request and create a plan as a JSON formatted list.
    - If the user asks about a wedding, use the 'find_available_venues' and 'get_moodboard' tasks.
    - If the user asks about fitness and savings, use the 'book_gym_class' and 'setup_auto_transfer' tasks. For the transfer, calculate the weekly amount needed to reach their goal in the specified time.
    
    Return ONLY the raw JSON for the plan and nothing else.
    """

    try:
        response = model.generate_content(instruction_prompt)
        plan_text = response.text
        match = re.search(r'\[.*\]', plan_text, re.DOTALL)
        if match:
            plan_json = match.group(0)
            plan = json.loads(plan_json)
            print("🤖 PLANNER: Gemini has returned a plan.")
            return plan
        else:
            raise ValueError("No JSON array found in the Gemini response.")

    except Exception as e:
        print(f"❌ PLANNER: Failed to generate plan from Gemini. Error: {e}")
        print("🤖 PLANNER: Using a hardcoded fallback plan.")
        # We will keep the wedding plan as the default fallback for now.
        return [
            {'agent': 'assistant_emma', 'task': 'find_available_venues',
                'params': {'max_price': 16000}},
            {'agent': 'style_guru_maya', 'task': 'get_moodboard',
                'params': {'style': 'classic'}}
        ]

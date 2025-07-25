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

    # FINAL UPDATE: We have added Tutor Sam's tools to the master list.
    instruction_prompt = f"""
    You are the planner for a multi-agent AI system. Your job is to analyze a user's request and create a step-by-step plan.
    
    The user's request is: "{user_prompt}"

    Here are the available tools:
    # Wedding Planning Tools
    - agent: "assistant_emma", task: "find_available_venues", params: {{{{ "max_price": "<budget in numbers>" }}}}
    - agent: "style_guru_maya", task: "get_moodboard", params: {{{{ "style": "<style>" }}}}
    
    # Fitness & Finance Tools
    - agent: "fitcoach_alex", task: "book_gym_class", params: {{{{ "class_name": "Weekly HIIT Session", "date": "Next Monday" }}}}
    - agent: "money_maven_sarah", task: "setup_auto_transfer", params: {{{{ "amount": "<calculated weekly amount>", "frequency": "weekly" }}}}

    # --- NEW TOOLS ADDED ---
    # Career & Education Tools
    - agent: "tutor_sam", task: "find_course", params: {{{{ "topic": "<course topic>" }}}}
    
    Analyze the user's request and create an initial plan as a JSON formatted list.
    - If the user asks about a wedding, use the wedding tools.
    - If the user asks about fitness and savings, use the fitness and finance tools.
    - If the user asks about career or learning, identify the topic and use the 'find_course' task.
    
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
        # Fallback remains the wedding plan
        return [
            {'agent': 'assistant_emma', 'task': 'find_available_venues',
                'params': {'max_price': 16000}},
            {'agent': 'style_guru_maya', 'task': 'get_moodboard',
                'params': {'style': 'classic'}}
        ]

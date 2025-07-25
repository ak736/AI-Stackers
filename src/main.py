from executor import execute_plan
from planner import generate_plan
import os


def run_wedding_demo():
    user_prompt = "Help me plan my wedding! My budget is $16,000 and I like a classic style."
    initial_plan = generate_plan(user_prompt)
    user_context = {}
    initial_results = execute_plan(initial_plan, user_context)

    venue_options = user_context.get('available_venues', [])
    if not venue_options:
        return {"error": "Emma couldn't find any venues."}

    choice_index = 0
    chosen_venue = venue_options[choice_index]
    user_context['chosen_venue_id'] = chosen_venue['id']
    user_context['chosen_venue_name'] = chosen_venue['name']

    booking_plan = [
        {'agent': 'assistant_emma', 'task': 'book_venue', 'params': {
            'venue_id': 'chosen_venue_id', 'venue_name': 'chosen_venue_name', 'date': '2025-10-26'}},
        {'agent': 'assistant_emma', 'task': 'draft_inquiry_email',
            'params': {'venue_name': 'chosen_venue_name'}}
    ]
    booking_results = execute_plan(booking_plan, user_context)

    # Instead of printing, we now build a dictionary to return
    final_results = {
        "moodboard": initial_results.get('get_moodboard'),
        "booking": booking_results.get('book_venue'),
        "email_draft": booking_results.get('draft_inquiry_email'),
        "chosen_venue_name": user_context['chosen_venue_name']
    }
    return final_results


def run_fitness_demo():
    user_prompt = "I want to get fit and save my first $1,000 in the next 8 weeks."
    plan = generate_plan(user_prompt)
    user_context = {}
    results = execute_plan(plan, user_context)
    # Return the results directly
    return {
        "gym_booking": results.get('book_gym_class'),
        "savings_setup": results.get('setup_auto_transfer')
    }


def run_career_demo():
    user_prompt = "I want to switch to a career in marketing. Find me a course to get started."
    initial_plan = generate_plan(user_prompt)
    user_context = {}
    initial_results = execute_plan(initial_plan, user_context)

    found_course = initial_results.get('find_course')
    if not found_course:
        return {"error": "Tutor Sam couldn't find a relevant course."}

    enrollment_plan = [{'agent': 'tutor_sam', 'task': 'enroll_in_course', 'params': {
        'course_id': found_course['id'], 'course_title': found_course['title']}}]
    enrollment_results = execute_plan(enrollment_plan, user_context)

    # Return the final enrollment status
    return {
        "enrollment": enrollment_results.get('enroll_in_course')
    }

from executor import execute_plan
from planner import generate_plan
import os

# --- DEMO SCENARIO 1: WEDDING ---


def run_wedding_demo():
    print("\n--- Running Wedding Planning Demo ---")
    user_prompt = "Help me plan my wedding! My budget for a venue is $16,000 and I like a classic style."
    print(f"USER: \"{user_prompt}\"")

    initial_plan = generate_plan(user_prompt)
    user_context = {}

    initial_results = execute_plan(initial_plan, user_context)

    print("\n--- MAIN: Simulating User Interaction ---")
    venue_options = user_context.get('available_venues', [])
    if not venue_options:
        print("MAIN: Emma couldn't find any venues. Ending demo.")
        return

    print("MAIN: Here are the venues Emma found. Please choose one:")
    for i, venue in enumerate(venue_options):
        print(f"  [{i+1}] {venue['name']} (${venue['price']})")

    choice_index = 0
    chosen_venue = venue_options[choice_index]
    user_context['chosen_venue_id'] = chosen_venue['id']
    user_context['chosen_venue_name'] = chosen_venue['name']
    print(f"USER: (Selects option {choice_index + 1}: {chosen_venue['name']})")

    booking_plan = [
        {'agent': 'assistant_emma', 'task': 'book_venue',
         'params': {'venue_id': 'chosen_venue_id', 'venue_name': 'chosen_venue_name', 'date': '2025-10-26'}},
        {'agent': 'assistant_emma', 'task': 'draft_inquiry_email',
         'params': {'venue_name': 'chosen_venue_name'}}
    ]
    booking_results = execute_plan(booking_plan, user_context)

    print("\n\n--- WEDDING DEMO: FINAL RESULTS ---")
    moodboard_path = initial_results.get('get_moodboard', 'Path not found')
    booking_status = booking_results.get(
        'book_venue', {}).get('status', 'failed')
    email_draft = booking_results.get(
        'draft_inquiry_email', 'Email draft failed.')

    if 'get_moodboard' in initial_results:
        print(f"✨ Moodboard: A style moodboard is ready at '{moodboard_path}'")
    if booking_status == 'confirmed':
        print(
            f"✅ Booking: Venue '{user_context['chosen_venue_name']}' is booked!")
        print("📅 To verify, check 'assets/emma/json/calendar_bookings.json'")

    print("\n📧 AI-Generated Email Draft:")
    print("-" * 30)
    print(email_draft)
    print("-" * 30)


# --- DEMO SCENARIO 2: FITNESS & FINANCE ---
def run_fitness_demo():
    print("\n--- Running Fitness & Finance Demo ---")
    user_prompt = "I want to get fit and save my first $1,000 in the next 8 weeks."
    print(f"USER: \"{user_prompt}\"")

    # The AI Planner will create the plan for Alex and Sarah
    plan = generate_plan(user_prompt)

    # We don't need user interaction mid-plan for this demo, so context is empty
    user_context = {}

    # The executor runs the tasks for Alex and Sarah
    results = execute_plan(plan, user_context)

    print("\n\n--- FITNESS & FINANCE DEMO: FINAL RESULTS ---")
    gym_booking = results.get('book_gym_class', {})
    savings_setup = results.get('setup_auto_transfer', {})

    if gym_booking.get('status') == 'confirmed':
        print(f"💪 Fitness Goal: Your '{gym_booking['class_name']}' is booked!")
        print(f"📅 To verify, check 'assets/alex/json/gym_bookings.json'")

    if savings_setup.get('status') == 'active':
        print(
            f"💰 Savings Goal: A {savings_setup['frequency']} auto-transfer of ${savings_setup['amount']} is now active!")
        print(f"📅 To verify, check 'assets/sarah/json/savings_transfers.json'")


# --- MAIN MENU ---
def main():
    """
    Main function to run the Squad AI interactive demo.
    """
    print("--- Welcome to the Squad AI Hackathon Demo ---")
    print("Which scenario would you like to run?")
    print("  [1] Wedding Planning Emergency")
    print("  [2] Fitness & Finance Overhaul")

    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            run_wedding_demo()
            break
        elif choice == '2':
            run_fitness_demo()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()

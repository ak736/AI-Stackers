# We need to import the function from our agent file
from agents.assistant_emma import find_available_venues
import os


def main():
    """
    This is the main function that runs our application.
    """
    print("--- Squad AI Hackathon Demo ---")
    print("User Prompt: 'Help me plan my wedding! My budget for a venue is $16,000.'")
    print("\n...Analyzing request...")

    # This simulates the system deciding to call Assistant Emma for the venue task.
    # We are calling the agent function directly for now.
    budget = 16000
    venue_options = find_available_venues(max_price=budget)

    print("\n--- Results ---")
    if venue_options:
        print(
            f"Here are the venue options Emma found within your ${budget} budget:")
        for venue in venue_options:
            # We construct the full path to the image for display purposes
            image_path = os.path.join(
                'assets', 'emma', 'img', venue['image_file'])
            print(f"  - Name: {venue['name']}")
            print(f"    Price: ${venue['price']}")
            # Later, a UI could display this image
            print(f"    Image: {image_path}")
            print("-" * 20)
    else:
        print("No venues were found within the specified budget.")

    print("\n--- Demo Step Complete ---")


# This is a standard Python practice to make the script runnable.
if __name__ == "__main__":
    main()

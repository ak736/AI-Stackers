import json
import os
import time

# Define the path to Alex's "database"
GYM_BOOKINGS_PATH = os.path.join('assets', 'alex', 'json', 'gym_bookings.json')


def book_gym_class(class_name: str, date: str) -> dict:
    """
    Simulates booking a gym class by writing to Alex's JSON file.
    """
    print(f"💪 FitCoach Alex: Booking '{class_name}' for {date}...")

    new_booking = {
        "booking_id": f"GYM{int(time.time())}",
        "class_name": class_name,
        "booking_date": date,
        "status": "confirmed"
    }

    try:
        # This assumes the file already exists and contains a list
        with open(GYM_BOOKINGS_PATH, 'r+') as f:
            bookings = json.load(f)
            bookings.append(new_booking)
            f.seek(0)
            f.truncate()
            json.dump(bookings, f, indent=4)

        print(
            f"✅ FitCoach Alex: Success! Class booked. ID: {new_booking['booking_id']}")
        return new_booking

    except Exception as e:
        print(f"❌ ERROR: Alex failed to write to his bookings file. {e}")
        return {"status": "failed"}

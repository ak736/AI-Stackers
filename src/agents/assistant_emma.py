import json
import os
import time  # To make the booking feel real

# (Keep the VENUES_FILE_PATH variable from before)
CALENDAR_FILE_PATH = os.path.join(
    'assets', 'emma', 'json', 'calendar_bookings.json')

# ... keep the find_available_venues function here ...


def book_venue(venue_id: int, venue_name: str, date: str) -> dict:
    """
    Simulates booking a venue by writing to a JSON file.
    This is our 'fake action'.
    """
    print(f"📅 Assistant Emma: Attempting to book '{venue_name}' for {date}...")

    # Create the new booking entry
    new_booking = {
        "booking_id": f"BK{int(time.time())}",  # Create a unique ID
        "venue_id": venue_id,
        "venue_name": venue_name,
        "booking_date": date,
        "status": "confirmed"
    }

    try:
        # Read the existing bookings
        with open(CALENDAR_FILE_PATH, 'r+') as f:
            bookings = json.load(f)
            bookings.append(new_booking)
            f.seek(0)  # Rewind to the start of the file
            json.dump(bookings, f, indent=4)  # Write the updated list back

        print(
            f"✅ Assistant Emma: Success! Booking confirmed. ID: {new_booking['booking_id']}")
        return new_booking

    except Exception as e:
        print(f"❌ ERROR: Emma failed to write to her calendar file. {e}")
        return {"status": "failed"}

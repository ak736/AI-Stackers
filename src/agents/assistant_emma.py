import json
import os
import time
# --- NEW IMPORTS ---
import google.generativeai as genai
from config import GEMINI_API_KEY

# --- CONFIGURE GEMINI FOR THIS AGENT ---
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')


# Define file paths relative to the project root
VENUES_FILE_PATH = os.path.join('assets', 'emma', 'json', 'venues.json')
CALENDAR_FILE_PATH = os.path.join(
    'assets', 'emma', 'json', 'calendar_bookings.json')


def find_available_venues(max_price: int) -> list:
    """
    Finds wedding venues from Emma's JSON file that are within the price range.
    """
    print(f"🤖 Assistant Emma: Searching for venues under ${max_price}...")
    try:
        budget = int(max_price)
        with open(VENUES_FILE_PATH, 'r') as f:
            all_venues = json.load(f)
        affordable_venues = [v for v in all_venues if v['price'] <= budget]
        if not affordable_venues:
            print("🤖 Assistant Emma: Found no venues within the budget.")
            return []
        print(
            f"🤖 Assistant Emma: Found {len(affordable_venues)} suitable venues.")
        return affordable_venues
    except Exception as e:
        print(f"❌ ERROR in find_available_venues: {e}")
        return []


def book_venue(venue_id: int, venue_name: str, date: str) -> dict:
    """
    Simulates booking a venue by writing to a JSON file.
    """
    print(f"📅 Assistant Emma: Attempting to book '{venue_name}' for {date}...")
    new_booking = {"booking_id": f"BK{int(time.time())}", "venue_id": venue_id,
                   "venue_name": venue_name, "booking_date": date, "status": "confirmed"}
    try:
        with open(CALENDAR_FILE_PATH, 'r+') as f:
            bookings = json.load(f)
            bookings.append(new_booking)
            f.seek(0)
            f.truncate()
            json.dump(bookings, f, indent=4)
        print(
            f"✅ Assistant Emma: Success! Booking confirmed. ID: {new_booking['booking_id']}")
        return new_booking
    except Exception as e:
        print(f"❌ ERROR: Emma failed to write to her calendar file. {e}")
        return {"status": "failed"}

# --- NEW AI-POWERED FUNCTION ---


def draft_inquiry_email(venue_name: str, couple_names: str = "The Happy Couple") -> str:
    """
    Uses the Gemini API to draft a professional inquiry email.
    """
    print(
        f"🤖 Assistant Emma: Thinking... Drafting an email to {venue_name}...")

    prompt = f"Draft a short, polite, and professional email to a wedding venue named '{venue_name}'. The email is from '{couple_names}'. It should confirm their interest and ask for the next steps regarding their recent booking. Keep it concise."

    try:
        response = model.generate_content(prompt)
        print("✅ Assistant Emma: Email draft generated.")
        return response.text
    except Exception as e:
        print(f"❌ ERROR: Emma failed to generate email draft. {e}")
        return "Error generating email."

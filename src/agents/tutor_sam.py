import json
import os
import time

# Define paths to Sam's "databases"
COURSES_DB_PATH = os.path.join('assets', 'sam', 'json', 'courses.json')
ENROLLMENTS_PATH = os.path.join(
    'assets', 'sam', 'json', 'enrolled_courses.json')


def find_course(topic: str) -> dict:
    """
    Finds a relevant course from the courses JSON database.
    """
    print(f"🎓 Tutor Sam: Searching for a course about '{topic}'...")
    try:
        with open(COURSES_DB_PATH, 'r') as f:
            all_courses = json.load(f)

        # Find the first course where the topic is in the title
        for course in all_courses:
            if topic.lower() in course['title'].lower():
                print(
                    f"✅ Tutor Sam: Found a relevant course: '{course['title']}'")
                return course

        print(f" Tutor Sam: Could not find a specific course for '{topic}'.")
        return {}

    except Exception as e:
        print(f"❌ ERROR: Sam could not read his course database. {e}")
        return {}


def enroll_in_course(course_id: int, course_title: str) -> dict:
    """
    Simulates enrolling in a course by writing to Sam's JSON file.
    """
    print(f"🎓 Tutor Sam: Enrolling you in '{course_title}'...")

    new_enrollment = {
        "enrollment_id": f"ENR{int(time.time())}",
        "course_id": course_id,
        "course_title": course_title,
        "enrollment_date": time.strftime("%Y-%m-%d"),
        "status": "enrolled"
    }

    try:
        with open(ENROLLMENTS_PATH, 'r+') as f:
            enrollments = json.load(f)
            enrollments.append(new_enrollment)
            f.seek(0)
            f.truncate()
            json.dump(enrollments, f, indent=4)

        print(
            f"✅ Tutor Sam: Success! You are now enrolled. ID: {new_enrollment['enrollment_id']}")
        return new_enrollment

    except Exception as e:
        print(f"❌ ERROR: Sam failed to write to his enrollments file. {e}")
        return {"status": "failed"}

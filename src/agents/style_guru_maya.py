import os
# --- NEW IMPORTS ---
import google.generativeai as genai
from config import GEMINI_API_KEY

# --- CONFIGURE GEMINI FOR THIS AGENT ---
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')


# Define paths to Maya's assets
IMAGE_ASSET_PATH = os.path.join('assets', 'maya', 'img')


def get_moodboard(style: str) -> dict:
    """
    Finds a pre-made moodboard image and uses Gemini to generate a creative description.
    """
    print(f"🎨 Style Guru Maya: Imagining a '{style}' moodboard...")

    # 1. Find the corresponding image file
    image_path = ""
    if style.lower() == 'classic':
        image_path = os.path.join(IMAGE_ASSET_PATH, 'moodboard_classic.jpg')
    elif style.lower() == 'modern':
        image_path = os.path.join(IMAGE_ASSET_PATH, 'moodboard_modern.jpg')
    else:
        # A fallback if the style is unknown
        image_path = os.path.join(IMAGE_ASSET_PATH, 'moodboard_classic.jpg')

    # 2. Use Gemini to generate a creative description
    prompt = f"You are an AI stylist. Describe a wedding moodboard with a '{style}' theme. Then, create a detailed prompt that an AI image generator like Midjourney or DALL-E could use to create this moodboard. Format your response as 'Description: [Your description] \n\nPrompt: [Your image prompt]'"

    try:
        response = model.generate_content(prompt)
        print("✅ Style Guru Maya: Creative vision generated.")
        # We return both the path to our dummy image and the AI-generated text
        return {
            "image_path": image_path,
            "ai_text": response.text
        }
    except Exception as e:
        print(f"❌ ERROR: Maya failed to generate creative text. {e}")
        return {
            "image_path": image_path,
            "ai_text": "Error generating description."
        }

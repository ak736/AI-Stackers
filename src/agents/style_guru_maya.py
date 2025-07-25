import os

# Define paths to Maya's assets
IMAGE_ASSET_PATH = os.path.join('assets', 'maya', 'img')


def get_moodboard(style: str) -> str:
    """
    Finds the path to a pre-made moodboard image based on style.
    """
    print(f"🎨 Style Guru Maya: Finding a '{style}' moodboard...")
    # In a real app, this might be more complex. Here, we map style to a file.
    if style == 'classic':
        return os.path.join(IMAGE_ASSET_PATH, 'moodboard_classic.jpg')
    elif style == 'modern':
        return os.path.join(IMAGE_ASSET_PATH, 'moodboard_modern.jpg')
    else:
        # A fallback
        return os.path.join(IMAGE_ASSET_PATH, 'default_moodboard.jpg')

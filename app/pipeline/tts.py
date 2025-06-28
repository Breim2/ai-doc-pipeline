# app/pipeline/tts.py

import pyttsx3
import os
from uuid import uuid4

# Step 3: Krumpli kockázása és hozzáadása
# Generates an audio file from the imported text

def generate_audio(text: str, output_dir="outputs") -> str:
    """
    Convert input text to speech and save as an mp3 file.
    Returns the file path of the generated audio.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)

        filename = f"{uuid4().hex[:8]}.mp3"
        output_path = os.path.join(output_dir, filename)

        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speaking speed
        engine.save_to_file(text, output_path)
        engine.runAndWait()

        return output_path
    except Exception as e:
        return f"[TTS] Error: {str(e)}"
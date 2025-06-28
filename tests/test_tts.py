import os
from app.pipeline.tts import generate_audio

def test_generate_audio_creates_file():
    # Provide sample summary text
    sample_text = "This is a test summary for the TTS system."

    # Call the TTS function
    audio_path = generate_audio(sample_text)

    # Assert that a path was returned and the file exists
    assert isinstance(audio_path, str), "TTS should return a string path"
    assert os.path.exists(audio_path), f"Expected audio file at {audio_path}"
    assert audio_path.endswith(".mp3"), "Audio file should be an MP3"
def test_dummy():
    assert 1 + 1 == 2

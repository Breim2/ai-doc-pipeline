# AI Document Pipeline

> A modular AI pipeline with FastAPI UI for OCR, text summarization, and text-to-speech.

---

## Overview

1. **Extract** text from the image via OCR
2. **Summarize** the extracted text with an AI model
3. **Convert** the summary to speech and return an audio file

Each step is modular and interdependent, with integrated logging, error handling, and task queueing.

---

## Project Structure

```
project_root/
├── app/
│   ├── pipeline/
│   │   ├── ocr.py          # OCR step
│   │   ├── summarizer.py   # Text summarization
│   │   └── tts.py          # Text-to-speech
│   ├── utils/
│   │   ├── logger.py       # Rotating logger
│   │   └── queue_manager.py# Async job queue
│   ├── web/
│   │   ├── interface.py    # FastAPI server
│   │   ├── templates/      # Jinja2 HTML files
│   │   └── static/         # CSS, favicon
│   └── main.py             # Pipeline integration (Paprikás Krumpli Recept)
├── outputs/                # Generated audio files
├── uploads/                # Uploaded images
├── logs/                   # Rotating logs
├── tests/                  # Unit tests for each module
├── start.bat              # Windows-compatible launch script
├── requirements.txt       # Project dependencies
├── README.md              # You're here
└── env/                   # Virtual environment
```

---

## How It Works

### Pipeline Stages

```python
# Step 1: Hagyma pirítása
raw_text = extract_text(image_path)

# Step 2: Paprika hozzáadása
summary = summarize_text(raw_text)

# Step 3: Krumpli kockázása és hozzáadása
audio_path = generate_audio(summary)
```

---

## Installation

1. **Clone the repo**
```bash
git clone https://github.com/Breim2/ai-doc-pipeline.git
cd ai-doc-pipeline
```

2. **Set up the environment**
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

3. **Run the app**
```bash
start.bat
```

---

## Web Interface

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) and:

- Upload a scanned document or image
- View the extracted and summarized text
- Listen to the generated MP3
- Click “View Logs” to monitor task processing

---

## Running Tests

Unit tests are included for all 3 core steps:
```bash
PYTHONPATH=. pytest tests/
```

---

## Dependencies

- `pytesseract`, `Pillow` – OCR
- `transformers`, `torch` – Text summarization
- `pyttsx3` – TTS
- `FastAPI`, `Jinja2`, `Uvicorn` – Web framework
- `pytest` – Unit testing
- `logging` – Rotating file logs

---

## AI Components

| Step        | Description              | Library        |
|-------------|--------------------------|----------------|
| OCR         | Image → Text             | `pytesseract`  |
| Summarizer  | Text → Summary           | `transformers` |
| TTS         | Summary → Audio (MP3)    | `pyttsx3`      |

---

## Special Notes

No pre-made demo integrations were used. All pipeline logic is built manually and documented clearly. External tools like HuggingFace Transformers are only used as **modules**, not as full demos.

---

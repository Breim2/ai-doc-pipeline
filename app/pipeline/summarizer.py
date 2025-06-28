# app/pipeline/summarizer.py

from transformers import pipeline

# Step 2: Paprika hozzáadása
# Summarize the extracted text

def summarize_text(text: str) -> str:
    try:
        if len(text.strip()) < 30:
            return "[Summarizer] Input too short to summarize."

        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        result = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return result[0]['summary_text']
    except Exception as e:
        return f"[Summarizer] Error: {str(e)}"
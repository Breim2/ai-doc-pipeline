
from app.pipeline.ocr import extract_text
from app.pipeline.summarizer import summarize_text
from app.pipeline.tts import generate_audio
from app.utils.logger import get_logger

logger = get_logger("MainPipeline")

def process_document(image_path: str) -> tuple[str, str]:
    logger.info("[Pipeline] Starting document processing...")

 # Step 1: Hagyma pirítása
    raw_text = extract_text(image_path)
    logger.info("[Pipeline] Extracted text: %s", raw_text[:200])

 # Step 2: Paprika hozzáadása
    summary = summarize_text(raw_text)
    logger.info("[Pipeline] Summary: %s", summary)

 # Step 3: Krumpli kockázása és hozzáadása
    audio_path = generate_audio(summary)
    logger.info("[Pipeline] Audio saved to: %s", audio_path)

    return summary, audio_path

# Step 4: Felöntés vízzel és főzés
if __name__ == "__main__":
    logger.info("[Pipeline] Running main pipeline...")
    test_image = "C:/Users/dolha/Documents/Programming/AI/ai_doc_pipeline/Bible.jpg"
    summary, audio = process_document(test_image)
    logger.info("[Pipeline] DONE.")

from PIL import Image
import pytesseract
import os

# Step 1: Hagyma pirítása
# Load the image and run OCR

def extract_text(image_path: str) -> str:
    """
    Extracts text from an image using Tesseract OCR.
    Returns the extracted text or a helpful error message.
    """
    try:
        if not os.path.exists(image_path):
            return "[OCR] Error: Image file not found."

        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip() if text.strip() else "[OCR] No text found."
    except Exception as e:
        return f"[OCR] Exception occurred: {str(e)}"
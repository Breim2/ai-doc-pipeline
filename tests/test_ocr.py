import os
from app.pipeline.ocr import extract_text

def test_ocr_extraction_on_sample_image():
    sample_image_path = "Bible.jpg"
    assert os.path.exists(sample_image_path), "Test image does not exist"

    extracted_text = extract_text(sample_image_path)

    assert isinstance(extracted_text, str), "OCR result should be a string"
    assert len(extracted_text.strip()) > 0, "Extracted text should not be empty"

    # Keywords that match your actual image content
    expected_keywords = ["beginning", "word", "god"]
    matched_keywords = [word for word in expected_keywords if word in extracted_text.lower()]
    assert matched_keywords, f"Expected at least one of {expected_keywords} in OCR result"

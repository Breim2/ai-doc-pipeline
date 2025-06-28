from app.pipeline.summarizer import summarize_text

def test_summarizer_basic():
    # Provide a known input text
    input_text = (
        "The Word Became Flesh. In the beginning was the Word, and the Word was with God, "
        "and the Word was God. He was with God in the beginning. Through him all things were made; "
        "without him nothing was made that has been made. In him was life, and that life was the light of all mankind."
    )

    summary = summarize_text(input_text)

    # Basic assertions
    assert isinstance(summary, str), "Summary should be a string"
    assert len(summary.strip()) > 0, "Summary should not be empty"
    
    # Optional: Check if the summary contains key elements
    keywords = ["word", "god", "life", "light"]
    matched = [kw for kw in keywords if kw in summary.lower()]
    assert matched, f"Expected keywords {keywords} to appear in summary"

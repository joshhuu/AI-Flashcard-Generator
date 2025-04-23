import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract all text from a PDF, preserving page breaks."""
    doc = fitz.open(pdf_path)
    try:
        pages = []
        for page in doc:
            text = page.get_text("text")  # more explicit
            pages.append(text)
        return "\n\n".join(pages)
    finally:
        doc.close()

import re
from PyPDF2 import PdfReader


def extract_pdf_text(filepath):
    reader = PdfReader(filepath)
    text_parts = []

    for page in reader.pages:
        page_text = page.extract_text() or ""
        cleaned = re.sub(r"\s+", " ", page_text).strip()
        if cleaned:
            text_parts.append(cleaned)

    text = "\n\n".join(text_parts)
    return text.strip()
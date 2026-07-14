import re
from docx import Document


def extract_docx_text(filepath):
    doc = Document(filepath)
    paragraphs = []

    for para in doc.paragraphs:
        cleaned = re.sub(r"\s+", " ", para.text).strip()
        if cleaned:
            paragraphs.append(cleaned)

    return "\n\n".join(paragraphs).strip()
import json
from groq import Groq
from config import Config
from services.groq_service import extract_document_structure

client = Groq(api_key=Config.GROQ_API_KEY)


def _fallback_flashcards(text):
    base = text.strip()[:220] or "the provided study material"
    return [
        {"question": "What is the main topic of the uploaded document?", "answer": f"The main topic is the content described in the document, especially the central idea around {base}."},
        {"question": "What is the biggest takeaway from the document?", "answer": "The main takeaway is the core message the author wants the reader to understand."},
        {"question": "What supporting ideas are most important?", "answer": "The supporting ideas are the explanation, evidence, examples, and evidence that reinforce the main point."},
        {"question": "How should the document be summarized?", "answer": "Summarize it by stating the purpose, main arguments, and key evidence in a short, clear form."},
        {"question": "What should a student focus on while studying it?", "answer": "Focus on the main arguments, important terms, and examples that connect the ideas together."},
        {"question": "What kind of questions should be asked about the document?", "answer": "Ask what the main idea is, why it matters, and how the examples support it."},
        {"question": "How can the document be studied effectively?", "answer": "Read it section by section, identify the main point of each section, and connect them to the whole document."},
        {"question": "What makes this document valuable?", "answer": "It provides a structured explanation of a topic with supporting details that build understanding."},
        {"question": "What is a helpful revision approach?", "answer": "Review the document by focusing on the key ideas first, then revisit the supporting examples."},
        {"question": "How would you explain this document simply?", "answer": "Explain it as a short description of the topic, its most important points, and why they matter."},
    ]


def generate_flashcards(text):
    structure = extract_document_structure(text)

    prompt = f"""
You are an AI study assistant.

Generate exactly 10 flashcards based on the document structure below.

Document title: {structure.get('title', 'Uploaded Document')}
Main topic: {structure.get('main_topic', '')}
Key points: {', '.join(structure.get('key_points', []))}
Examples: {', '.join(structure.get('examples', []))}
Conclusion: {structure.get('conclusion', '')}

Return ONLY valid JSON.

Example:

[
    {{
        "question":"...",
        "answer":"..."
    }}
]
"""

    try:
        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ],

            temperature=0.3

        )

        return json.loads(response.choices[0].message.content)
    except Exception:
        return _fallback_flashcards(text)
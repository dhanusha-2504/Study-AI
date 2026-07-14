import json
import re

from groq import Groq
from config import Config

client = Groq(api_key=Config.GROQ_API_KEY)


def _heuristic_document_structure(text):
    cleaned = (text or "").strip()
    if not cleaned:
        return {
            "title": "Uploaded Document",
            "main_topic": "The uploaded document",
            "key_points": ["Main idea of the document"],
            "examples": ["Example discussed in the document"],
            "conclusion": "The document emphasizes the topic and its importance.",
        }

    lines = [line.strip() for line in cleaned.splitlines() if line.strip()]
    title = lines[0] if lines else "Uploaded Document"

    sentences = re.split(r"(?<=[.!?])\s+", cleaned)
    main_topic = sentences[0] if sentences else cleaned[:180]
    if len(main_topic) > 220:
        main_topic = main_topic[:220] + "..."

    key_points = []
    for line in lines:
        if line.startswith(("-", "•", "*")) or re.match(r"^\d+\.", line):
            key_points.append(line.lstrip("-*•1234567890. "))
        elif line.lower().startswith(("objective", "objective:", "significance", "importance", "need", "scope", "basic concept")):
            key_points.append(line)

    if not key_points:
        key_points = [
            "Main idea of the document",
            "Important definitions and concepts",
            "Examples and supporting details",
        ]

    examples = []
    for line in lines:
        if "example" in line.lower() or line.startswith(("-", "•", "*")):
            examples.append(line)
    if len(examples) > 2:
        examples = examples[:2]
    elif not examples:
        examples = ["Example discussed in the document", "A practical case related to the topic"]

    conclusion = ""
    for sentence in reversed(sentences):
        if len(sentence.split()) > 4:
            conclusion = sentence
            break
    if not conclusion:
        conclusion = "The document emphasizes the topic and its importance."

    return {
        "title": title,
        "main_topic": main_topic,
        "key_points": key_points,
        "examples": examples,
        "conclusion": conclusion,
    }


def extract_document_structure(text):
    structure = _heuristic_document_structure(text)

    if not Config.GROQ_API_KEY:
        return structure

    prompt = f"""
You are a document analyzer.

Read the following study material and extract the most important structure from it.
Return ONLY valid JSON with this exact shape:

{{
  "title": "...",
  "main_topic": "...",
  "key_points": ["...", "..."],
  "examples": ["...", "..."],
  "conclusion": "..."
}}

Study Material:
{text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        content = response.choices[0].message.content.strip()
        parsed = json.loads(content.replace("```json", "").replace("```", "").strip())

        if isinstance(parsed, dict):
            for key in ("title", "main_topic", "key_points", "examples", "conclusion"):
                value = parsed.get(key)
                if value:
                    structure[key] = value
        return structure
    except Exception:
        return structure


def _fallback_summary(text):
    topic = text.strip()[:220] or "the provided study material"
    return (
        "Detailed Study Summary\n\n"
        f"Main idea: {topic}\n\n"
        "Key concepts:\n"
        "- Focus on the central themes and the main arguments presented in the document.\n"
        "- Review the important definitions, examples, and supporting evidence.\n"
        "- Connect each section back to the overall purpose of the document.\n\n"
        "Study approach:\n"
        "- Break the material into smaller sections and study each one carefully.\n"
        "- Test your understanding by explaining the content in your own words.\n"
        "- Revisit difficult points and compare them with the main ideas in the document."
    )


def generate_summary(text):
    structure = extract_document_structure(text)

    prompt = f"""
You are an expert study assistant.

Create a detailed summary of this document using the extracted structure.

Document title: {structure.get('title', 'Uploaded Document')}
Main topic: {structure.get('main_topic', '')}
Key points: {', '.join(structure.get('key_points', []))}
Examples: {', '.join(structure.get('examples', []))}
Conclusion: {structure.get('conclusion', '')}

Rules:
- Use simple language.
- Use bullet points.
- Mention important concepts.
- Keep it concise but complete.
- Return only the summary.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4
        )
        return response.choices[0].message.content
    except Exception:
        return _fallback_summary(text)
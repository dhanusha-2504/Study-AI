from groq import Groq
from config import Config
from services.groq_service import extract_document_structure

client = Groq(api_key=Config.GROQ_API_KEY)


def _fallback_schedule(text):
    return (
        "Detailed Study Schedule\n\n"
        "Day 1:\n"
        "- Read the uploaded document once and identify the main purpose.\n"
        "- Highlight the key sections and write a short summary of each part.\n\n"
        "Day 2:\n"
        "- Study the major ideas, definitions, and examples in the document.\n"
        "- Make short notes on the core message and the supporting evidence.\n\n"
        "Day 3:\n"
        "- Focus on the sections that explain the topic most clearly.\n"
        "- Try to explain the document in your own words without looking at the text.\n\n"
        "Day 4:\n"
        "- Practice answering questions based on the main ideas and evidence.\n"
        "- Mark the ideas that still feel unclear.\n\n"
        "Day 5:\n"
        "- Revisit weak points and connect them to the overall document.\n"
        "- Review the examples and important supporting details.\n\n"
        "Day 6:\n"
        "- Test yourself with short recall questions about the whole document.\n"
        "- Improve your summary using the points you remember best.\n\n"
        "Day 7:\n"
        "- Revise everything and prepare a final summary of the document.\n"
        f"- Final focus: {text[:220]}"
    )


def generate_schedule(text):
    structure = extract_document_structure(text)

    prompt = f"""
You are an AI study planner.

Create a study schedule for the document described below.

Document title: {structure.get('title', 'Uploaded Document')}
Main topic: {structure.get('main_topic', '')}
Key points: {', '.join(structure.get('key_points', []))}
Examples: {', '.join(structure.get('examples', []))}
Conclusion: {structure.get('conclusion', '')}

Rules:
- Divide into Day 1, Day 2, Day 3...
- Keep each day manageable.
- Mention revision day.
- Keep it concise.
- Return only the schedule.
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
        return _fallback_schedule(text)
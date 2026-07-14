import json
from groq import Groq
from config import Config
from services.groq_service import extract_document_structure

client = Groq(api_key=Config.GROQ_API_KEY)


def _fallback_quiz(text):
    return [
        {"question": "What is the main topic of the uploaded document?", "options": ["A. The main idea of the document", "B. A random side note", "C. The title page only", "D. A conclusion without evidence"], "answer": "A. The main idea of the document"},
        {"question": "What should a student focus on when studying this document?", "options": ["A. The central ideas and supporting evidence", "B. Only the formatting", "C. The page number", "D. The decorative layout"], "answer": "A. The central ideas and supporting evidence"},
        {"question": "Which part of the document is most important for understanding it?", "options": ["A. The introduction and main arguments", "B. The blank spaces", "C. The footer", "D. The page border"], "answer": "A. The introduction and main arguments"},
        {"question": "What is the purpose of the supporting examples in the document?", "options": ["A. To clarify the main idea", "B. To distract the reader", "C. To replace the summary", "D. To hide the main message"], "answer": "A. To clarify the main idea"},
        {"question": "What is the best study approach for this kind of document?", "options": ["A. Read section by section and summarize each part", "B. Only read the first page", "C. Skip the examples", "D. Memorize the layout"], "answer": "A. Read section by section and summarize each part"},
        {"question": "How can you test whether you understood the document?", "options": ["A. Explain the main ideas in your own words", "B. Ignore the topic", "C. Only look at the title", "D. Memorize the page count"], "answer": "A. Explain the main ideas in your own words"},
        {"question": "What is the value of reviewing the document multiple times?", "options": ["A. It improves understanding and memory", "B. It creates confusion", "C. It makes the content shorter", "D. It removes the main point"], "answer": "A. It improves understanding and memory"},
        {"question": "Which question is most helpful when analyzing the document?", "options": ["A. What is the main message?", "B. What color is the page?", "C. How long is the title?", "D. Which font is used?"], "answer": "A. What is the main message?"},
        {"question": "What should a strong summary include?", "options": ["A. The main points and evidence", "B. Only random details", "C. No examples", "D. Blank statements"], "answer": "A. The main points and evidence"},
        {"question": "How should difficult sections be handled?", "options": ["A. Break them into smaller parts and review them carefully", "B. Ignore them completely", "C. Only read the first sentence", "D. Skip to the end"], "answer": "A. Break them into smaller parts and review them carefully"},
        {"question": "Why are examples important in a document?", "options": ["A. They make the main ideas clearer", "B. They replace the summary", "C. They make the document shorter", "D. They confuse the reader"], "answer": "A. They make the main ideas clearer"},
        {"question": "What is a good revision habit for this document?", "options": ["A. Review it regularly and test yourself", "B. Read it only once", "C. Ignore the details", "D. Avoid note-taking"], "answer": "A. Review it regularly and test yourself"},
        {"question": "What should be remembered after studying the document?", "options": ["A. The main purpose and supporting ideas", "B. Only the first sentence", "C. The page layout", "D. The heading style"], "answer": "A. The main purpose and supporting ideas"},
        {"question": "What is the best way to explain the document to others?", "options": ["A. In simple language using the main ideas", "B. By repeating the title only", "C. By speaking randomly", "D. By skipping examples"], "answer": "A. In simple language using the main ideas"},
        {"question": "What makes a study session effective?", "options": ["A. Focused review of the key points", "B. Reading without thinking", "C. Avoiding questions", "D. Skipping revision"], "answer": "A. Focused review of the key points"},
        {"question": "How can a learner stay engaged with the document?", "options": ["A. By asking questions about the main ideas", "B. By ignoring the examples", "C. By reading only the first line", "D. By skipping the summary"], "answer": "A. By asking questions about the main ideas"},
        {"question": "What is the final goal of studying this document?", "options": ["A. Understand its purpose and key message", "B. Memorize only the title", "C. Learn the page count", "D. Only review the first page"], "answer": "A. Understand its purpose and key message"},
    ]


def generate_quiz(text):
    structure = extract_document_structure(text)

    prompt = f"""
Generate 18 multiple choice questions based on the document structure below.

Document title: {structure.get('title', 'Uploaded Document')}
Main topic: {structure.get('main_topic', '')}
Key points: {', '.join(structure.get('key_points', []))}
Examples: {', '.join(structure.get('examples', []))}
Conclusion: {structure.get('conclusion', '')}

Return ONLY JSON.

Example:

[
 {{
   "question":"...",
   "options":["A","B","C","D"],
   "answer":"A"
 }}
]
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
            temperature=0.2
        )

        content = response.choices[0].message.content.strip()

        # Remove markdown if present
        content = content.replace("```json", "").replace("```", "").strip()

        return json.loads(content)
    except Exception:
        return _fallback_quiz(text)
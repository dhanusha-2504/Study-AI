from flask import Blueprint, request, jsonify

from services.flashcard_service import generate_flashcards

flashcard_bp = Blueprint("flashcards", __name__)


@flashcard_bp.route("/generate-flashcards", methods=["POST"])
def flashcards():

    data = request.get_json()

    text = data.get("text")

    cards = generate_flashcards(text)

    return jsonify({

        "success": True,

        "flashcards": cards

    })
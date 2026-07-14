from flask import Blueprint, request, jsonify

from services.quiz_service import generate_quiz

quiz_bp = Blueprint("quiz", __name__)


@quiz_bp.route("/generate-quiz", methods=["POST"])
def quiz():

    data = request.get_json()

    text = data.get("text")

    quiz = generate_quiz(text)

    return jsonify({
        "success": True,
        "quiz": quiz
    })
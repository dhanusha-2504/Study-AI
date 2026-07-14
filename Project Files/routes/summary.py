from flask import Blueprint, request, jsonify
from services.groq_service import generate_summary

summary_bp = Blueprint("summary", __name__)

@summary_bp.route("/generate-summary", methods=["POST"])
def summary():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "No data received"
        }), 400

    text = data.get("text")

    if not text:
        return jsonify({
            "success": False,
            "error": "Study material is required"
        }), 400

    try:
        summary = generate_summary(text)

        return jsonify({
            "success": True,
            "summary": summary
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
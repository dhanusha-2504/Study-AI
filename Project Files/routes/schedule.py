from flask import Blueprint, request, jsonify

from services.schedule_service import generate_schedule

schedule_bp = Blueprint("schedule", __name__)


@schedule_bp.route("/generate-schedule", methods=["POST"])
def schedule():

    print("REQUEST RECEIVED")

    data = request.get_json()

    print(data)

    text = data.get("text")

    result = generate_schedule(text)

    print("GENERATED")

    return jsonify({
        "success": True,
        "schedule": result
    })
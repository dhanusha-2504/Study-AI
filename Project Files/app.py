import os
import socket

from flask import Flask
from flask_cors import CORS
from routes.upload import upload_bp
from routes.summary import summary_bp
from routes.flashcards import flashcard_bp
from routes.quiz import quiz_bp
from routes.schedule import schedule_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(summary_bp, url_prefix="/api")
app.register_blueprint(upload_bp, url_prefix="/api")
app.register_blueprint(flashcard_bp, url_prefix="/api")
app.register_blueprint(quiz_bp, url_prefix="/api")
app.register_blueprint(schedule_bp, url_prefix="/api")


@app.route("/")
def home():
    return {
        "status": "success",
        "message": "StudyAI Backend Running 🚀"
    }


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }



# temp
@app.route("/test-schedule")
def test_schedule():

    from services.schedule_service import generate_schedule

    result = generate_schedule(
        "Machine Learning is a subset of Artificial Intelligence. It enables computers to learn from data."
    )

    return {
        "result": result
    }


def get_available_port(start_port=5000):
    port = int(os.getenv("PORT", start_port))
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind(("0.0.0.0", port))
                return port
            except OSError:
                port += 1


if __name__ == "__main__":
    port = get_available_port()
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)
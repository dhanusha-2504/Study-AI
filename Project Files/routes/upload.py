from flask import Blueprint, request, jsonify

from services.upload_service import save_uploaded_file
from services.pdf_parser import extract_pdf_text
from services.docx_parser import extract_docx_text

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload-material", methods=["POST"])
def upload_material():

    if "file" not in request.files:
        return jsonify({
            "success": False,
            "error": "No file uploaded"
        }), 400

    file = request.files["file"]

    filepath = save_uploaded_file(file)

    if file.filename.lower().endswith(".pdf"):
        text = extract_pdf_text(filepath)

    elif file.filename.lower().endswith(".docx"):
        text = extract_docx_text(filepath)

    else:
        return jsonify({
            "success": False,
            "error": "Only PDF and DOCX files are supported."
        }), 400

    return jsonify({
        "success": True,
        "filename": file.filename,
        "text": text,
        "text_length": len(text.split())
    })
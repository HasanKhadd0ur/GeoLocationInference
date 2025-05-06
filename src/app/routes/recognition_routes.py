from flask import Blueprint, request, jsonify

from app.services.recognition_service import recognize_locations

recognition_bp = Blueprint("recognition", __name__)

@recognition_bp.route("/", methods=["POST"])
def recognize():
    text = request.json.get("text", "")
    strategy = request.args.get("strategy", "llm")
    result = recognize_locations(text, strategy)
    return jsonify(result)

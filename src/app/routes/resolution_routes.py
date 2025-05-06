from flask import Blueprint, request, jsonify
from app.services.resolution_service import geocode_text, detect_common_location

resolution_bp = Blueprint("resolution", __name__)

@resolution_bp.route("/geocode", methods=["POST"])
def geocode():
    text = request.json.get("text", "")
    result = geocode_text(text)
    return jsonify(result)

@resolution_bp.route("/common-location", methods=["POST"])
def common_location():
    texts = request.json.get("texts", [])
    result = detect_common_location(texts)
    return jsonify(result)

from flask import Blueprint, request, jsonify

from app.core.factory.services_factory import get_location_recognizer_service

recognition_bp = Blueprint('recognition', __name__)
location_service = get_location_recognizer_service("llm")

@recognition_bp.route('/extract-message-location', methods=['POST'])
def extract_message_location():
    data = request.get_json()
    text = data.get("text") or data.get("message", "")
    # print(data)
    if not text:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    try:
        locations = location_service.extract_message_location(text)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify( locations)

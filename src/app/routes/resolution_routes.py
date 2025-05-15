from flask import Blueprint, request, jsonify
from app.core.factory.services_factory import get_location_resolver_service

resolution_bp = Blueprint('resolution', __name__)
resolution_service =get_location_resolver_service("nominatim")

@resolution_bp.route('/extract-event-location', methods=['POST'])
def extract_event_location():
    data = request.get_json()
    messages = data

    if not messages:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    location = resolution_service.extract_event_location(messages)
    return jsonify(location)

@resolution_bp.route('/geocode', methods=['GET'])
def geocode():
    location = request.args.get('location')
    
    if not location:
        return jsonify({"error": "Missing 'location' query parameter"}), 400

    coords = resolution_service.geocode(location)
    return jsonify(coords)

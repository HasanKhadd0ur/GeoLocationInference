from flask import Blueprint, request, jsonify
from app.location.factory.services_factory import get_location_resolver_service

resolution_bp = Blueprint('resolution', __name__)
resolution_service =get_location_resolver_service()

@resolution_bp.route('/geocode', methods=['GET'])
def geocode():
    
    location = request.args.get('location')
    print(location)
    if not location:
        return jsonify({"error": "Missing 'location' query parameter"}), 400

    coords = resolution_service.geocode(location)
    return jsonify(coords)

# app/api/admin_config_routes.py
from flask import Blueprint, request, jsonify

from app.location.factory.location_service_config import LocationServiceConfigManager

config_bp = Blueprint("config", __name__, url_prefix="/config")

@config_bp.route("/location-services/config", methods=["PUT"])
def update_location_service_config():
    data = request.get_json()

    recognizer_key = data.get("recognizer_key")
    resolver_key = data.get("resolver_key")

    config = LocationServiceConfigManager()

    if recognizer_key:
        config.set_recognizer_key(recognizer_key)
    if resolver_key:
        config.set_resolver_key(resolver_key)

    return jsonify({
        "message": "Location service configuration updated",
        "recognizer_key": config.get_recognizer_key(),
        "resolver_key": config.get_resolver_key()
    }), 200

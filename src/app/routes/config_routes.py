from flask import Blueprint, request, jsonify
from app.location.registry.resolution_service_registry import ServicesRegistry

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


@config_bp.route("/location-services/recognizers", methods=["GET"])
def get_available_recognizers():
    recognizers = list(ServicesRegistry._recognizers.keys())
    return jsonify({"recognizers": recognizers})

@config_bp.route("/location-services/resolvers", methods=["GET"])
def get_available_resolvers():
    resolvers = list(ServicesRegistry._resolvers.keys())
    return jsonify({"resolvers": resolvers})


@config_bp.route("/location-services/config", methods=["GET"])
def get_current_location_service_config():
    config = LocationServiceConfigManager()
    return jsonify({
        "recognizer_key": config.get_recognizer_key(),
        "resolver_key": config.get_resolver_key()
    })

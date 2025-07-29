from flask import Flask
from app.routes.recognition_routes import recognition_bp
from app.routes.resolution_routes import resolution_bp
from app.routes.config_routes import config_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(recognition_bp, url_prefix="/recognition")
    app.register_blueprint(resolution_bp, url_prefix="/resolution")

    app.register_blueprint(config_bp, url_prefix="/config")

    return app

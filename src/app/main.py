from flask import Flask
from app.routes.recognition_routes import recognition_bp
from app.routes.resolution_routes import resolution_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(recognition_bp, url_prefix="/recognition")
app.register_blueprint(resolution_bp, url_prefix="/resolution")

if __name__ == "__main__":
    app.run(debug=True)

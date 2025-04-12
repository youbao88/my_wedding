import os
from flask import Flask, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .database import init_db

def get_ip():
    # Use the X-Real-IP header set by Nginx, fallback to REMOTE_ADDR
    return request.headers.get("X-Real-IP", get_remote_address())

limiter = Limiter(get_ip, app=None, default_limits=['2 per 5 minutes'])

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')  # Load SECRET_KEY from environment
    CORS(app, resources={r"/*": {"origins": "https://minhaoandtao.love"}})  # Allow CORS for the frontend URL
    init_db()  # Initialize the database
    limiter.init_app(app)  # Initialize Flask-Limiter
    from .routes import routes_blueprint
    app.register_blueprint(routes_blueprint)
    return app

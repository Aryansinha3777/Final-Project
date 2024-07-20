from flask import Blueprint, jsonify
errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resourse not found"}),404

@errors.app_errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad request"}),400

@errors.app_errorhandler(500)
def interval_error(error):
    return jsonify({"error": "Internal server error"}),500

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
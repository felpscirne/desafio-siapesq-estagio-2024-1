import os
from flask import Flask
from flask_jwt_extended import JWTManager
from Backend.shared.db import db
from Backend.auth.routes import auth
from Backend.locations.routes import locations
import secrets


def create_app():
    app = Flask(__name__)
    db_url = os.getenv('DATABASE_URL', 'postgresql://localhost/postgres')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(16)
    jwt = JWTManager(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(locations, url_prefix='/locations')
    
    return app


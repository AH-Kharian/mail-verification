from flask import Flask
from src.routes.auth import auth_bp
from src.config import Config
from src.extensions.db import init_db


def create_app():
    app=Flask(__name__)
    print(app.jinja_loader.searchpath)

    app.config.from_object(Config)
    init_db()
    app.register_blueprint(auth_bp,url_prefix='/verify-email')
    return app
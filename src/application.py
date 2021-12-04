from flask import Flask
from src.controllers import AuthenticationController
import src.database


def create_app(db_uri: str) -> Flask:
    app = Flask(__name__)
    app.config["MONGO_URI"] = db_uri
    src.database.mongo.get_mongo().init_app(app)

    # Register the routes
    app.add_url_rule("/login", methods=["POST"], view_func=AuthenticationController.login)
    app.add_url_rule("/signup", methods=["POST"], view_func=AuthenticationController.register)

    return app

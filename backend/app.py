from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
from dotenv import load_dotenv

from config import Config
from src.controllers.championship.championship_controller import blp as championship_blp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    CORS(app)
    api = Api(app)

    # Registra blueprints
    api.register_blueprint(championship_blp)

    return app


if __name__ == '__main__':
    load_dotenv()
    app = create_app()
    app.run(debug=True)

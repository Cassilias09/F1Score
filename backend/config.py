import os


class Config:
    # Flask
    FLASK_APP = 'app'
    FLASK_DEBUG = bool(os.getenv('FLASK_DEBUG', 0))
    FLASK_ENV = os.getenv('FLASK_ENV') or 'development'
    SECRET_KEY = os.getenv('SECRET_KEY')
    URL_PREFIX = os.getenv('URL_PREFIX', default="/api")

    # Flask-Smorest
    API_TITLE = 'F1Score API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.0'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/swagger'
    OPENAPI_SWAGGER_UI_URL = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/'

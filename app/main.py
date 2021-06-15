import sys

from flask import Flask, Blueprint

import utils.settings as settings
from api.endpoints.v1.user import ns as user_namespace
from werkzeug.middleware.proxy_fix import ProxyFix

from api.restplus import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_port=1, x_for=1, x_host=1, x_prefix=1)


def configure_app(flask_app):
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def get_api_v1_blueprint():
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(user_namespace)
    return blueprint


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint_v1 = get_api_v1_blueprint()
    flask_app.register_blueprint(blueprint_v1)


def main():
    initialize_app(app)
    try:
        app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=settings.FLASK_DEBUG)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()

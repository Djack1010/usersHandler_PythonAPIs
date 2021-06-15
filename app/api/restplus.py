from flask_restplus import Api

from utils import settings

api = Api(version="0.1", title="TEST",
          description="Manage interaction with user db")


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    print(f"Exception: {e}")
    if not settings.FLASK_DEBUG:
        return {'message': message}, 500

# Flask settings
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
FLASK_DEBUG = False  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# DB settings
DB_USER = 'root'
DB_PASSWORD = 'CHOOSE_A_PASSWORD'
# DB_HOST = 'db'
DB_HOST = 'localhost'
# DB_PORT = '3306'
DB_PORT = '32000'
DB_DATABASE = 'login'
DB_CONFIG = {
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST,
    'port': DB_PORT,
    'database': DB_DATABASE
}

# Execution settings

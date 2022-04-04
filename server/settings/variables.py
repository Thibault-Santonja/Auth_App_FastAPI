import json


try:
    with open('credentials.json') as json_file:
        credentials = json.load(json_file)
except FileNotFoundError:
    with open('../../credentials.json') as json_file:
        credentials = json.load(json_file)

# API settings
API_HOST = "0.0.0.0"
API_PORT = 3200
API_ROOT = "/api/v1"

# Database settings
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "Auth_App"
DB_TYPE = "postgresql"
DB_USER = credentials.get('database').get('username')
DB_PASS = credentials.get('database').get('password')

import json
import os
from pyseto import Key

try:
    with open('credentials.json') as json_file:
        credentials = json.load(json_file)
except FileNotFoundError:
    credentials = {
      "database": {
        "password": "postgres",
        "username": "postgres"
      }
    }

# API settings
API_HOST = "0.0.0.0"
API_PORT = 3200
API_ROOT = "/api/v1"

# Database settings
DB_HOST = "db"  # localhost
DB_PORT = 5432
DB_NAME = "Auth_App"
DB_TYPE = "postgresql"
DB_USER = credentials.get('database').get('username')
DB_PASS = credentials.get('database').get('password')

# Security settings
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# openssl rand -hex 32
if 'PASETO_PRIVATE_KEY' in os.environ and 'PASETO_PUBLIC_KEY' in os.environ:
    private_key = os.environ['PASETO_PRIVATE_KEY']
    public_key = os.environ['PASETO_PUBLIC_KEY']
else:
    private_key = b"-----BEGIN PRIVATE KEY-----\nMC4CAQAwBQYDK2VwBCIEILTL+0PfTOIQcn2VPkpxMwf6Gbt9n4UEFDjZ4RuUKjd0\n" \
                  b"-----END PRIVATE KEY----- "
    public_key = b"-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAHrnbu7wEfAP9cGBOAHHwmH4Wsot1ciXBHwBBXQ4gsaI=\n" \
                 b"-----END PUBLIC KEY-----"
PASETO_PRIVATE_KEY = Key.new(version=4, purpose="public", key=private_key)
PASETO_PUBLIC_KEY = Key.new(version=4, purpose="public", key=public_key)

import os
from app import app

PORT = os.environ.get('APP_PORT') or 5001
HOST = os.environ.get('APP_HOST') or '0.0.0.0'

print(PORT, HOST, os.environ.get('APP_PORT'),os.environ.get('APP_HOST'))

app.run(host=HOST, port=int(PORT))
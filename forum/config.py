import os

SECRET_KEY = "dev"
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = f"{BASE_PATH}/database.sqlite"

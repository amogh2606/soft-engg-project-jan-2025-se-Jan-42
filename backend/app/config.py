SQLALCHEMY_DATABASE_URI = 'sqlite:///app_db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'EukLT2BvSm49J72OQ0Udsidhl6QyBvQWczpqVXg6CrI'
WTF_CSRF_ENABLED = False
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = '246487170862000527440433179734659260030'
SECURITY_REDIRECT_BEHAVIOR = 'spa'
SECURITY_FLASH_MESSAGES = False
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

google_api_key = os.getenv("GOOGLE_API_KEY")
print(f"Using Google API Key: {google_api_key}")  # Debugging purpose


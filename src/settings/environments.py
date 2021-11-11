import os
from dotenv import load_dotenv

load_dotenv()

FB_PRIVATE_KEY = os.getenv('FB_PRIVATE_KEY')
FB_PRIVATE_KEY_ID = os.getenv('FB_PRIVATE_KEY_ID')
FB_CLIENT_EMAIL = os.getenv('FB_CLIENT_EMAIL')
APP_WRAPPER_API_KEY = os.getenv('APP_WRAPPER_API_KEY')
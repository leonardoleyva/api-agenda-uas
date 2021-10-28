import os
from dotenv import load_dotenv

load_dotenv()

FB_PRIVATE_KEY_DEV = os.getenv('FB_PRIVATE_KEY_DEV')
FB_PRIVATE_KEY_ID_DEV = os.getenv('FB_PRIVATE_KEY_ID_DEV')
FB_CLIENT_EMAIL_DEV = os.getenv('FB_CLIENT_EMAIL_DEV')

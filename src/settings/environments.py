import os
from dotenv import load_dotenv

load_dotenv()

FB_PRIVATE_KEY = os.environ['FB_PRIVATE_KEY'].replace(r'\n', '\n')
FB_PRIVATE_KEY_ID = os.getenv('FB_PRIVATE_KEY_ID')
FB_CLIENT_EMAIL = os.getenv('FB_CLIENT_EMAIL')

SMTP_SERVER_CRED_EMAIL = os.getenv('SMTP_SERVER_CRED_EMAIL')
SMTP_SERVER_CRED_PASSWORD = os.getenv('SMTP_SERVER_CRED_PASSWORD')
import firebase_admin
from firebase_admin import credentials
from ..settings.environments import FB_CLIENT_EMAIL, FB_PRIVATE_KEY, FB_PRIVATE_KEY_ID
import json
import codecs


class App:
    def __init__(self) -> None:
        serviceAccountJSON = self.__getServiceAccountJSON()
        cred = credentials.Certificate(serviceAccountJSON)
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)

    def __getServiceAccountJSON(self):
        file = open('serviceAccountKey.json', 'r')
        fileJSON = json.loads(file.read())
        fileJSON["private_key"] = codecs.decode(
            FB_PRIVATE_KEY, "unicode_escape")
        # fileJSON["private_key"] = FB_PRIVATE_KEY
        fileJSON["private_key_id"] = FB_PRIVATE_KEY_ID
        fileJSON["client_email"] = FB_CLIENT_EMAIL
        return fileJSON

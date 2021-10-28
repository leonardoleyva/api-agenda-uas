import firebase_admin
from firebase_admin import credentials, firestore
from settings.environments import FB_PRIVATE_KEY_DEV, FB_PRIVATE_KEY_ID_DEV
import json
import codecs


class DBConnection:
    def __init__(self) -> None:
        serviceAccountJSON = self.__getServiceAccountJSON()
        cred = credentials.Certificate(serviceAccountJSON)
        firebase_admin.initialize_app(cred)
        self.__db = firestore.client()

    def getDBInstance(self):
        return self.__db

    def __getServiceAccountJSON(self):
        file = open('serviceAccountKey.json', 'r')
        fileJSON = json.loads(file.read())
        fileJSON["private_key"] = codecs.decode(FB_PRIVATE_KEY_DEV, "unicode_escape")
        fileJSON["private_key_id"] = FB_PRIVATE_KEY_ID_DEV
        return fileJSON

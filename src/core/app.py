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
        fileJSON["private_key"] = self.__string_escape(FB_PRIVATE_KEY)
        fileJSON["private_key_id"] = FB_PRIVATE_KEY_ID
        fileJSON["client_email"] = FB_CLIENT_EMAIL
        return fileJSON

    def __string_escape(s, encoding='utf-8'):
        return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
                # Perform the actual octal-escaping decode
                .decode('unicode-escape')
                .encode('latin1')         # 1:1 mapping back to bytes
                .decode(encoding))        # Decode original encoding

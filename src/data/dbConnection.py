from firebase_admin import firestore
from google.cloud.firestore_v1.base_client import BaseClient

from ..core.app import App


class DBConnection(App):
    def __init__(self) -> None:
        super().__init__()
        self.__db: BaseClient = firestore.client()

    def getDBInstance(self) -> BaseClient:
        return self.__db

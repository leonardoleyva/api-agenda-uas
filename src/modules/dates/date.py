from ...data.dbConnection import DBConnection
from google.cloud.firestore_v1.collection import CollectionReference
from google.cloud.firestore_v1.document import DocumentReference


class Date(DBConnection):
    __collection = 'dates'

    def __init__(self) -> None:
        super().__init__()
        self.__datesCollection: CollectionReference = self.getDBInstance(
        ).collection(self.__collection)

    def createOne(self, data) -> bool:
        try:
            self.__datesCollection.add(data)
            print('Date was created successfully')
            return True
        except:
            print('Something went wrong with request to the server')
            return False

    def searchAll(self):
        try:
            docs: list[DocumentReference] = self.__datesCollection.get()

            print('Dates was gotten successfully')
            return {
                'status': True,
                'dates': docs,
            }
        except:
            print('Something went wrong with request to the server')
            return {
                'status': False,
            }

    def deleteOne(self, id: str) -> bool:
        try:
            self.__datesCollection.document(id).delete()
            print('Date was declined successfully')
            return True
        except:
            print('Something went wrong with request to the server')
            return False

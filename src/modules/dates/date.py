from ..SMTP.smtp import SMTP
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
                'dates': [],
            }

    def deleteOne(self, id: str) -> bool:
        try:
            self.__datesCollection.document(id).delete()
            print('Date was declined successfully')
            return True
        except:
            print('Something went wrong with request to the server')
            return False

    def acceptOne(self, id: str, timeForDate: str) -> bool:
        try:
            self.__datesCollection.document(id).update(
                {'status': 'accepted', 'timeForDate': timeForDate})

            date = self.__datesCollection.document(id).get().to_dict()
            email = date['email']
            firstName = date['firstName']
            lastName = date['lastName']
            subject = 'Servicio Social (Vicerrectoria) - Confirmación de cita'

            message = f'Por este medio se le comunica a {firstName} {lastName} que su solicitud de cita fue confirmada para la hora -> {timeForDate}'

            SMTP.sendMail(email, subject, message)

            print('Date was accepted successfully')
            return True
        except:
            print('Something went wrong with request to the server')
            return False

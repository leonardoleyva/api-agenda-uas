from ...data.dbConnection import DBConnection


class Date(DBConnection):
    __collection = 'dates'

    def __init__(self) -> None:
        super().__init__()

    def createOne(self, data):
        try:
            self.getDBInstance().collection(self.__collection).add(data)
            print('Date was created successfully')
            return True
        except:
            print('Something went wrong with request to the server')
            return False

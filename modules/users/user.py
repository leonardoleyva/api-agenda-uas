from data.dbConnection import DBConnection


class User(DBConnection):
    __collection = 'users'

    def __init__(self) -> None:
        super().__init__()

    # def createUser(self, data):
    #     self.getDBInstance().collection(self.__collection).add(data)

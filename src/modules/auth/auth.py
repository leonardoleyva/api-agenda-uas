import hashlib
import os

from firebase_admin.auth import Client, UserNotFoundError
from firebase_admin.exceptions import FirebaseError
from google.cloud.firestore_v1.collection import CollectionReference
from ...data.dbConnection import DBConnection


class Auth(DBConnection):
    __collection = 'users'

    def __init__(self) -> None:
        super().__init__()
        self.__usersCollection: CollectionReference = self.getDBInstance(
        ).collection(self.__collection)

    def signUp(self, email: str, password: str):
        try:
            queryMatch = self.__usersCollection.where(
                'email', '==', email).get()

            if len(queryMatch) > 0:
                return {
                    'status': False,
                    'message': f'El usuario {email} ya esta registrado'
                }

            salt = os.urandom(32)  # A new salt for this user
            key = self.__getHashKey(password, salt)

            params = {'email': email, 'password': key, 'rb': salt}
            self.__usersCollection.add(params)

            return {
                'status': True,
                'message': f'Usuario {email} registrado exitosamente'
            }
        except FirebaseError as err:
            print(err)
            return {
                'status': False,
                'message': 'Error del servidor al intentar registrar un usuario'
            }

    def signIn(self, email: str, password: str):
        try:
            queryMatch = self.__usersCollection.where(
                'email', '==', email).get()

            if len(queryMatch) == 0:
                return {
                    'status': False,
                    'message': f'El usuario {email} no esta registrado'
                }

            user = queryMatch[0].to_dict()

            if self.__getHashKey(password, user['rb']) != user['password']:
                return {
                    'status': False,
                    'message': 'Credenciales incorrectas'
                }

            return {
                'status': True,
                'message': 'Sesion iniciada exitosamente'
            }
        except FirebaseError as err:
            print(err)
            return {
                'status': False,
                'message': 'Error del servidor al intentar iniciar sesion'
            }

    def __getHashKey(self, password, salt):
        return hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), salt, 100000)

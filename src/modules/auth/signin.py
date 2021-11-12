from ..response import handleResponse
from .auth import Auth

def signIn(body):
    req = Auth().signIn(body['email'], body['password'])

    response = handleResponse(req['status'], req['message'], {})
    return response
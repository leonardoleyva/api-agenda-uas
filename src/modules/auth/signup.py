from ..response import handleResponse
from .auth import Auth


def signUp(body):
    req = Auth().signUp(body['email'], body['password'])

    response = handleResponse(req['status'], req['message'], {})
    return response

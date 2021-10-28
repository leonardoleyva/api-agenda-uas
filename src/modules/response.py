def handleResponse(status: bool, message: str, body):
    isSuccessfully = status == True
    return {
        'head': {
            'status': 'okay' if isSuccessfully else 'error',
            'code': 200 if isSuccessfully else 400,
            'message': message,
        },
        'body': {
            'response': body,
        }
    }

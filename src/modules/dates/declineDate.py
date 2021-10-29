from .date import Date
from ..response import handleResponse


def declineDate(body):
    reqStatus = Date().deleteOne(body['id'])

    message = "Cita rechazada exitosamente" if reqStatus == True else "No se pudo rechazar la cita, inténtelo más tarde"

    response = handleResponse(reqStatus, message, {})

    return response

from .date import Date
from ..response import handleResponse


def acceptDate(body):
    reqStatus = Date().acceptOne(body['id'], body['timeForDate'])

    message = "Cita confirmada exitosamente" if reqStatus == True else "No se pudo confirmar la cita, inténtelo más tarde"

    response = handleResponse(reqStatus, message, {})

    return response

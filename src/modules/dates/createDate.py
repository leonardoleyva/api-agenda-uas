from .date import Date
from ..response import handleResponse


def createDate(body):
    reqStatus = Date().createOne({ **body, 'status': 'pending' })

    message = "Cita creada exitosamente" if reqStatus == True else "No se pudo crear la cita, inténtelo más tarde"

    response = handleResponse(reqStatus, message, {})

    return response

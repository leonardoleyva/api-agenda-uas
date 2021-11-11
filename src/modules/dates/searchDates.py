from .date import Date
from ..response import handleResponse
from datetime import datetime


def searchDates():
    req = Date().searchAll()

    message = "Listado de citas" if req['status'] == True else "No se pudo conseguir el listado de citas, inténtelo más tarde"

    dateToday = datetime.now().isoformat().split('T')[0]

    dates = []
    for date in req['dates']:
        dateDict = date.to_dict()
        dateYYMMDD = dateDict['date'].split('T')[0]
        if dateYYMMDD >= dateToday:
            dates.append({**dateDict, 'id': date.id})

    response = handleResponse(req['status'], message, dates)

    return response

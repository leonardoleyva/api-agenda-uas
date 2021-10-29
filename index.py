from flask import Flask, request, jsonify
from src.modules.dates.declineDate import declineDate
from src.modules.dates.searchDates import searchDates
from src.modules.dates.createDate import createDate

app = Flask(__name__)


@app.route('/')
def index():
    return "Running on port 5000..."


@app.route('/create-date', methods=['POST'])
def createNewDate():
    body = request.json
    response = createDate(body)
    return jsonify(response)


@app.route('/search-dates', methods=['POST'])
def getAllDates():
    response = searchDates()
    return jsonify(response)


@app.route('/decline-date', methods=['POST'])
def declineOneDate():
    body = request.json
    response = declineDate(body)
    return jsonify(response)

app.run()

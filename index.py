from flask import Flask, request, jsonify
from src.modules.auth.signin import signIn
from src.modules.auth.signup import signUp

from src.modules.auth.auth import Auth
from src.modules.dates.acceptDate import acceptDate
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


@app.route('/accept-date', methods=['POST'])
def confirmDate():
    body = request.json
    response = acceptDate(body)
    return jsonify(response)


@app.route('/sign-up', methods=['POST'])
def signup():
    body = request.json
    response = signUp(body)
    return jsonify(response)


@app.route('/sign-in', methods=['POST'])
def login():
    body = request.json
    response = signIn(body)
    return jsonify(response)


if __name__ == '__main__':
    app.run()

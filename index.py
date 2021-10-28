from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Running on port 5000..."


app.run()

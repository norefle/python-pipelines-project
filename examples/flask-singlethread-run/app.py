# app.py - a minimal flask api using flask_restful
from flask import Flask

app = Flask(__name__)


@app.route("/infinite")
def block_forever():
    while True:
        # Infinite loop
        pass


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return "I'm here", 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080, threaded=False)

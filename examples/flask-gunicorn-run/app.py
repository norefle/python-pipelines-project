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

from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response

app = Starlette(debug=False)

@app.route("/")
async def index(request):
    return Response("I'm here", status_code=200)

@app.route("/infinite")
async def block_forever(request):
    while True:
        # Infinite loop
        pass


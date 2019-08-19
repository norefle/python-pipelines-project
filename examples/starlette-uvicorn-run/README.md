# Skink/Starlette-Uvicorn-Run

Example of a single-threaded Starlette web server behind Uvicorn.

## Build

To build the example with docker, simply run:

```
docker build -t skink/starlette-uvicorn-run .
```

## Run

First, build the docker image (see Build).
Second, run the docker image and expose 8080 port:

```
docker run -p 8080:8080 skink/starlette-uvicorn-run:latest
```
Last, open in your browser `localhost:8080` to see the greetings.

## Test

To test the single-threaded nature of the server, first, run (see Run) the server
and open the following page in your browser `localhost:8080/infinite`.
Then in a new tab open the initial page `localhost:8080`.

You won't be able to see the results in neither of them since the "infinite" endpoint
blocks the only thread of the application.


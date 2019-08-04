# Skink/Flask-Gunicorn-Run

Example of a single-threaded Gunicorn + Flask web server.

## Build

To build the example with docker, simply run:

```
docker build -t skink/flask-gunicorn-run .
```

## Run

First, build the docker image (see Build).
Second, run the docker image and expose 8080 port:

```
docker run -p 8080:8080 skink/flask-gunicorn-run:latest
```
Last, open in your browser `localhost:8080` to see the greetings.

## Test

To test the multi-threaded nature of the server, first, run (see Run) the server
and open the following page in your browser `localhost:8080/infinite`.
Then in a new tab open the initial page `localhost:8080`.

You will see that the page is still available.

However, if you open `localhost:8080/infinite` the second time and then try
to open `localhost:8080` you won't be able to see the index page, since both
threads are block. The number 2 comes from the configuration we ran the server with,
for more details see the [Dockerfile](Dockerfile)
and [Gunicorn documentation](http://docs.gunicorn.org/en/stable/settings.html).
Also in the same docker file you will see that the gunicorn server has been
executed with `timeout` argument, which tells the server to kill blocked workers
after selected number of seconds. It's 5 in our configuration,
hence if you wait for more than 5 seconds you will be able to see
`localhost:8080` again.

This is the _main_ benefit of having WSGI server in fron of the pure flask application,
it handles a lot of technical routines for you.
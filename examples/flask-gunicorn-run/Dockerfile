FROM python:3.7-alpine

RUN apk add dumb-init

# Configure
ENV POETRY_VERSION=0.12.17
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml /app/

RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

RUN cat /app/poetry.lock

# Install app
COPY . /app

# Run
EXPOSE 8080

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080", "--workers", "2", "--timeout", "5"]

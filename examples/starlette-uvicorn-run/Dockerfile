FROM python:3.7-alpine

RUN apk add --no-cache --virtual=.build-dependencies g++ make

RUN apk add dumb-init libstdc++

# Configure
ENV POETRY_VERSION=0.12.17
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml /app/

RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

RUN apk del .build-dependencies

# Install app
COPY . /app

# Run
EXPOSE 8080

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1"]


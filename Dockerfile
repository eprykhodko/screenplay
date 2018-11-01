FROM python:3.7.1-alpine3.8

RUN apk add --update --no-cache g++ libxslt-dev

WORKDIR /app

RUN python -m pip -q --no-cache-dir install poetry && \
    python -m poetry config settings.virtualenvs.create false

COPY pyproject* ./
RUN python -m poetry install -q --no-interaction --no-dev && \
    python -m poetry cache:clear -n --no-interaction pypi --all

RUN apk del g++

COPY . .


ENTRYPOINT  ["poetry", "run", "swc"]

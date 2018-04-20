FROM python:3.6.5-alpine3.7
COPY . /
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r requirements.txt

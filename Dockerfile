FROM python:3.10-alpine3.13 AS builder
WORKDIR /app 
COPY requirements.txt /app

RUN apk update && apk add --update --no-cache \
    postgresql-dev \
    libpq-dev \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \ 
    RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
EXPOSE 80
ENTRYPOINT ["sh", "entrypoint.sh"]



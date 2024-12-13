FROM python:3.10-alpine3.13 AS builder
ENV PYTHONUNBUFFERED=1
WORKDIR /app 


RUN apk add --update --no-cache \
    alpine-sdk \
    postgresql-dev \    
    libffi-dev    

COPY requirements.txt /app    
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
EXPOSE 80
ENTRYPOINT ["sh", "entrypoint.sh"]



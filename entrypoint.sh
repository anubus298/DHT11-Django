#!/bin/sh
# entrypoint.sh
python3 manage.py collectstatic --noinput
gunicorn CoreRoot.asgi:application --bind 0.0.0.0:80 -k uvicorn.workers.UvicornWorker

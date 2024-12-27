#!/bin/bash

# Install some dependencies
# apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     libffi-dev \
#     python3-pip

# Install Python dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Create Vercel-compatible output directory
mkdir -p .vercel/output/static
cp -r staticfiles/ .vercel/output/static/

# Apply database migrations
python3 manage.py makemigrations
python3 manage.py migrate

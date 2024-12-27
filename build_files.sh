#!/bin/bash
echo "Installing pip if required..."
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
echo "Building the project..."
python3 -m pip install setuptools wheel
python3 -m pip install -r requirements.txt
echo "Make Migration..."
echo "Collect Static..."
mkdir static
python3 manage.py collectstatic --noinput --clear
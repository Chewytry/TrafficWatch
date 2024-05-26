#!/bin/sh

set -e

echo "Running migrations..."
python manage.py migrate
python manage.py makemigrations

echo "Starting application..."
exec "$@"

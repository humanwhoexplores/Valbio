#!/bin/bash
set -e
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn strike_backend.wsgi --bind=0.0.0.0:${PORT:-8000}

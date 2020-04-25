#!/bin/ash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn -c lti_inspector/gunicorn.conf.py lti_inspector.wsgi:application

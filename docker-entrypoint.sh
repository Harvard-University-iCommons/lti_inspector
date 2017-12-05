#!/bin/bash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
touch /code/logs/gunicorn.log
touch /code/logs/access.log
tail -n 0 -f /code/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn lti_inspector.wsgi:application \
    --name lti_inspector \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=debug \
    --log-file=/code/logs/gunicorn.log \
    --access-logfile=/code/logs/access.log \
    "$@"

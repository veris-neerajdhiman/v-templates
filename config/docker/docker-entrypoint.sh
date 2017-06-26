#!/bin/bash

# Prepare log files and start outputting logs to stdout
#touch /var/log/gunicorn.log
#touch /var/log/access.log
#tail -n 0 -f /var/log/*.log &

# Start Gunicorn processes
#echo Starting Gunicorn.
#exec gunicorn config.wsgi:application \
#    --name v-templates \
#    --bind 0.0.0.0:80 \
#    --workers 3 \
#    --log-level=info \
#    "$@"
exec python manage.py runserver 0.0.0.0:80

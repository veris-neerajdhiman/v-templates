#!/bin/bash

# Prepare log files and start outputting logs to stdout
touch /var/logs/gunicorn.log
touch /var/logs/access.log
tail -n 0 -f /var/logs/*.log &

# Start Gunicorn processes
#echo Starting Gunicorn.
exec gunicorn config.wsgi:application \
    --name v-templates \
    --bind 0.0.0.0:80 \
    --workers 3 \
    --log-level=info \
    "$@"

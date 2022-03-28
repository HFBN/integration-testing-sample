#!/usr/bin/env bash
export IS_DEBUG=${DEBUG:-false}
exec gunicorn --bind 0.0.0.0:5000 --access-logfile - --error-logfile - --timeout 600 run:flask_app
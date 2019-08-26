#!/usr/bin/env bash

python manage.py migrate
gunicorn -w 4 -b 0.0.0.0:$PORT angrydevblog.wsgi

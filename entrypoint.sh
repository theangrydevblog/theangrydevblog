#!/usr/bin/env bash

python manage.py migrate
gunicorn -w $(expr 2 \* $(nproc) + 1) -b 0.0.0.0:$PORT angrydevblog.wsgi

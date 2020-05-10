#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn -w $(expr 2 \* $(nproc) + 1) \
	-c python:gunicorn_config \
	angrydevblog.wsgi 

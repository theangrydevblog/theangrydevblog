#!/usr/bin/env bash

npm run start
npm run start-react
python manage.py collectstatic --noinput

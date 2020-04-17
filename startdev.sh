#!/usr/bin/env bash

docker run -d --env-file .env --net host --name dev theangrydevblog

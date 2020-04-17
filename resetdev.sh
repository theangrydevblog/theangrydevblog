#!/usr/bin/env bash

docker kill dev && docker rm dev
docker build -t theangrydevblog .


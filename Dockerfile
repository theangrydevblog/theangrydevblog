FROM python:3.8-slim-buster
MAINTAINER Prithaj Nath

RUN apt update

# GCC and other essentials
RUN apt install -y libpq-dev build-essential

# Networking tools
RUN apt install -y \
	traceroute \
	curl \
	iputils-ping \
	bridge-utils \
	dnsutils \
	netcat-openbsd \
	jq \
	postgresql-client \
	nmap \
	net-tools \
    	&& rm -rf /var/lib/apt/lists/*

RUN NODE_VERSION=13 && curl -sL https://deb.nodesource.com/setup_${NODE_VERSION}.x  | bash - \
	&& apt install -y nodejs

WORKDIR /usr/bin/theangrydev

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9000

ENTRYPOINT ["./entrypoint.sh"]

FROM ubuntu:20.04

# use bash shell as default
SHELL ["/bin/bash", "-c"]

# disable interactive terminal
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

# install python, pip and pipenv
RUN apt-get update && \
    apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

RUN wget https://www.python.org/ftp/python/3.9.11/Python-3.9.11.tgz && \
	tar -xf Python-3.9.11.tgz && \
	cd Python-3.9.11 && \
	./configure --enable-optimizations && \
	make -j 12 && \
	make altinstall

# add the user Motoko, tribute to https://en.wikipedia.org/wiki/Motoko_Kusanagi
RUN useradd --create-home --no-log-init --system  motoko && \
	echo "motoko	ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers
USER motoko
WORKDIR /home/motoko

# set some local environment variables
ENV LANG en_US.UTF-8

RUN	python3.9 -m pip --no-cache-dir install --user --upgrade pip && \
	python3.9 -m pip --no-cache-dir install --user --upgrade pipenv

RUN echo "alias pipenv=\"python3.9 -m pipenv\"" >> ~/.bashrc

LABEL com.circleci.preserve-entrypoint=true

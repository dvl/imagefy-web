FROM python:3.5

MAINTAINER André Luiz <contato@xdvl.info>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    gettext

RUN pip install -U pip
RUN pip install "libsass==0.11.1"

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

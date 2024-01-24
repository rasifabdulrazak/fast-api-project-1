FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt

COPY ./app /app

WORKDIR /app

RUN apt-get update \
    && /py/bin/pip install -r /tmp/requirements.txt \
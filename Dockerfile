# pull official base image
FROM python:3.12-slim-bookworm

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./PictureMe /usr/src/PictureMe
WORKDIR /usr/src/PictureMe
#COPY .env .
COPY superuser.py .

RUN apt-get update && \
    apt-get -y install --no-install-recommends curl && \
    apt-get -y install --no-install-recommends default-mysql-client && \
    apt-get -y install --no-install-recommends default-libmysqlclient-dev && \
    apt-get -y install --no-install-recommends python3-dev && \
    apt-get -y install --no-install-recommends gcc && \
    apt-get -y install --no-install-recommends pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# create static directory
RUN python manage.py collectstatic --no-input

ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_PASSWORD
ENV DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL
ENV DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME
ENV DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD

# pull official base image
FROM python:3.10-slim-bullseye

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./PictureMe /usr/src/PictureMe
WORKDIR /usr/src/PictureMe
#COPY .env .
COPY superuser.py .

#    apt-get upgrade -y && \ is left out for now
RUN apt-get update && \
    apt-get -y install curl && \
    apt-get -y install default-libmysqlclient-dev && \
    apt-get -y install libpq-dev  && \
    apt-get -y install python3-dev && \
    apt-get -y install gcc && \
    apt-get -y install pkg-config && \
    apt-get clean

# cleanup
RUN apt-get clean && apt-get autoclean && apt-get autoremove

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
# Установка суперпользователя с использованием переменных окружения

#RUN python manage.py createsuperuser --no-input
##migration
#RUN python manage.py makemigrations
#RUN python manage.py migrate --no-input

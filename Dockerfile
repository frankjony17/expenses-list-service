# base image
FROM python:3.10

RUN apt-get update -y && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# setup environment variable
ENV SERVICE_HOME=/usr/src/app/service

# set work directory
RUN mkdir -p $SERVICE_HOME

# where your code lives
WORKDIR $SERVICE_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $SERVICE_HOME

# run this command to install all dependencies
RUN pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000
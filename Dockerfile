# base image
FROM python:3.10

RUN apt-get update -y && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# setup environment variable
ENV SERVICE_HOME=/usr/src/apps/api

# set work directory
RUN mkdir -p $SERVICE_HOME
RUN mkdir $SERVICE_HOME/staticfiles
RUN mkdir $SERVICE_HOME/mediafiles

# where your code lives
WORKDIR $SERVICE_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install flake8==5.0.4

# copy whole project to your docker home directory.
COPY . $SERVICE_HOME

RUN flake8 .

# run this command to install all dependencies
RUN pip install -r requirements.txt

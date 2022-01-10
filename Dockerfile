FROM python:3.9-alpine3.15
# ensure output from python is sent straight to the terminal without buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Sets the container's working directory to /code
WORKDIR /code
# Copy requirements.txt
COPY requirements.txt /code/
#  Install build essentails
RUN apk add --no-cache --update build-base
# Pip install requirements
RUN pip install -r requirements.txt
# Copy source code to container
COPY . /code/

# piggee
Pig Latin translation microservice

# PIGGEE
Welcome to the pig latin translation microservice.

## Table of Contents
- [Technologies Used](#technologies-used)
- [How To Get Started](#how-to-get-started)
- [API Project Structure](#api-project-structure)
- [API Documentation](#api-documentation)
    - [Translate](#translate)
- [Testing](#testing)
- [Docker](#docker)
- [Kubrnetes](#kubernetes)


## Technologies Used
- Python3
- Django


## How To Get Started
- git clone `git@github.com:bmwachajr/piggee.git`
- Create a virtualenv `python3 -m virtualenv venv`
- Activate a virtualenv: `python3 -m virtualenv venv`
    - Mac OS / Linux: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate`
- Install Project dependecies `pip3 install -r requirements.txt`
- Copy .env `cp core/.env.example core/.env` and set SECRET_KEY value
- Run the server: `python3 manage.py runserver`
- Access the app on `http://0.0.0.0:8000/`

## Using the python cli client:
You can use a python client script to send requests (through API) to your application.
- Use [docker-compose](#docker) to [Kubrnetes](#kubernetes) to spin up the microservice.
- From the root directory of the project, navigate into the client module. `cd client`
- Start the python client. `python3 -m python_client.py`

## API Project Structure
The microservice api structure has been set up inside the `/api/` path on the project. In this folder you should create a specific project for each endpoint on the API. 

For example:
```
core/
api/
    piglatin
```

## Endpoint Documentation

### Translate
#### Request

    `POST /translate/piglatin/`

    Allow: POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
        "text": ""
    }

#### Response

    HTTP 201 Created
    Allow: POST, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "text": "",
        "translation": "",
        "codec": "Pig Latin"
    }

## Testing
In order to test the apps created you can use the following command:

        python manage.py test core.translate.<endpoint>

For example, to test the events endpoint than you can type: `python manage.py test core.translate.pig_latin`


## Docker
In order to use docker compose to test the app:
- Copy .env `cp core/.env.example core/.env` and set SECRET_KEY value
- Build the app `docker-compose build`
- Run the app `docker-compose up`
- Access the app on `http://0.0.0.0:8000/translate/pig_latin`

## Kubernetes
In order to use docker compose to test the app:
- Spin up K8 service `kubectl create -f deployment.yml`
- Access the app on `http://localhost:8000/translate/pig_latin`


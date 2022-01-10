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
- Run the server: `python3 manage.py runserver`

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

    HTTP 200 OK
    Allow: POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "text": "",
        "translation": "",
        "codec": "pig latin"
    }

## Testing
In order to test the apps created you can use the following command:

        python manage.py test core.translate.<endpoint>

For example, to test the events endpoint than you can type: `python manage.py test core.translate.pig_latin`


## Docker

## Kubernetes

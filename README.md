# How to run the application

## Prerequisites

- Python 3.6 or up
- virtualenv installed 

## Steps

- install the requriements using req.txt file in api folder
    ``` pip install -r req.txt ```
Note: Its better to use a virtualenv
- run the app using following commands
    ``` export FLASK_APP=src/api.py  ```
    ``` flask create-db ``` 
    ``` flask run ```

## Endpoints

### Register
endpoint: http://localhost:5000/auth/signup

sample payload:

``` 
{ 
    "email": "valid@email.com",
    "password": "somepw"
    "first_name": "chathuranga"
```

### Login
endpoint: http://localhost:5000/auth/login


``` 
{ 
    "email": "valid@email.com",
    "password": "somepw"
```

## Run as a docker container

Make sure docker is installed

cd in to root folder (where the dockerfile is at)

``` 
sudo docker build -t myapp:latest .
```

```
sudo docker run -d -p 5000:5000 myapp
```

server will be served from 0.0.0.0:5000 (or the port that the command is matched to )

Please do contact me on contact@chathuranga.com for any issue. 

Cheers!
Chathuranga Bandara
www.chathuranga.com



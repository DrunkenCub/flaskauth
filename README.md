# How to run the application

## Prerequisites

- Python 3.6 or up
- virtualenv installed 

## Steps

- install the requriements using req.txt file in api folder
    ``` pip install -r req.txt ```
Note: Its better to use an virtualenv
- run the app using folloeing commands
    ``` export FLASK_APP=src/api.py  ```
    ``` flask create-db ``` 
    ``` flask run ```

## Endpoints

### Register
sample payload:
``` 
{ 
    "email": "valid@email.com",
    "password": "somepw"
    "first_name": "chathuranga"
```

### Login

``` 
{ 
    "email": "valid@email.com",
    "password": "somepw"
```

Please do contact me on contact@chathuranga.com for any issue. 

Cheers!
Chathuranga Bandara
www.chathuranga.com



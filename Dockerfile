FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

COPY ./api/req.txt /var/www/req.txt

RUN pip install -r /var/www/req.txt

COPY ./api /app 

EXPOSE 5000

ENV FLASK_APP src/api.py

# Havent implemented checking the db exists 
CMD flask create-db

CMD flask run --host=0.0.0.0
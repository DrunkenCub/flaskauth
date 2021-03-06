import jwt
import datetime
import re

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from .api import db, bcrypt
from .config import *

from .mixins.db_mixin import OutputMixin


class User(OutputMixin, db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(256), nullable=True)


    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('Email address is required')

        if not re.match(EMAIL_REGEX, email):
            raise AssertionError('Email provided is not valid.')
        return email

    def set_password(self, password): 
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, pw):
        self.password = bcrypt.check_password_hash(self.password, pw)

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise ('Signature expired. Please log in again.')
        except jwt.InvalidTokenError:
            raise Exception('Invalid token. Please log in again.')
        except Exception as e:
            raise e
            
    



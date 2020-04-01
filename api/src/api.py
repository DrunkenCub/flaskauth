from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from .config import DB_CON_STRING


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_CON_STRING

# according to https://github.com/pallets/flask-sqlalchemy/issues/365 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

CORS(app)

#
import click

@app.cli.command('create-db')
def create_db():
    try:
        db.create_all()
    except Exception as e:
        raise e
#


# Registering enpoints
from .endpoints.auth import auth_bp
from .endpoints.user import user_bp

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)









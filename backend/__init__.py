import click
from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restplus import reqparse, abort, Api, Resource
from backend.models.db import db
from backend.models.user import User
from backend.models.server import Server
from backend.models.journalentry import JournalEntry
from werkzeug.security import generate_password_hash,check_password_hash
from backend.routes import blueprint
from werkzeug.middleware.proxy_fix import ProxyFix

import json
import logging

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/marcus.broberg/development/serverjournal/test.db'
app.config['SECRET_KEY'] = 'bad_key'
login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(blueprint)
app.wsgi_app = ProxyFix(app.wsgi_app)
db.init_app(app)
migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    logging.info("load_user")
    return User.query.filter_by(id=user_id).first()

@app.cli.command()
@click.argument('username')
@click.argument('email')
@click.argument('password')
@click.argument('firstname')
@click.argument('surname')
def create_user(username,email, password, firstname,surname):
    #Checks if uses exist
    user = User.query.filter_by(username=username).all()
    if len(user)!=0:
        print("User exists")
        return 0
    hashed_password = generate_password_hash(password)
    user = User(username=username,email=email, password=hashed_password, firstname=firstname, surname=surname)
    db.session.add(user)
    db.session.commit()


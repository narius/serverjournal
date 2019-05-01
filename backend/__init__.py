from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_restplus import reqparse, abort, Api, Resource
from backend.models.db import db
from backend.models.user import User
from backend.models.server import Server
from backend.models.journalentry import JournalEntry
import json
import logging

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/marcus.broberg/development/serverjournal/test.db'
db.init_app(app)
migrate = Migrate(app, db)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)

@api.route('/hello')
class HelloWorld(Resource):
   def get(self):
      logging.info("Hello world.get")
      return json.loads(json.dumps(['hello world']))


app.register_blueprint(blueprint)

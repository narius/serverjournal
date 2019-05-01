from flask import Flask, Blueprint
from flask_restplus import reqparse, abort, Api, Resource
import json
import logging
app = Flask(__name__)


blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)

@api.route('/hello')
class HelloWorld(Resource):
   def get(self):
      logging.info("Hello world.get")
      return json.loads(json.dumps(['hello world']))


app.register_blueprint(blueprint)

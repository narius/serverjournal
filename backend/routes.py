from flask import Blueprint, request, session,g
from flask_login import current_user
from flask_restplus import reqparse, abort, Api, Resource
import logging
import json

from backend.authentication.loginapi import LoginApi

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)



#@api.route('/hello','/hello/<name>', endpoint='hello')
#@api.doc(params={'name': 'A name'})
class HelloWorld(Resource):

    def get(self, name='no name'):
        """Returns list of blog categories."""
        logging.info("Hello world.get")
        logging.debug(session)
        logging.debug(current_user)
        logging.info("is anonu")
        logging.debug(current_user.is_anonymous)
        logging.info("is auth")
        logging.debug(current_user.is_authenticated)
        return json.loads(json.dumps(['hello ' + name + 'current user: '+str(current_user)]))


endpoints = [
    (['/hello'], HelloWorld),
    (['/hello/<name>'], HelloWorld),
    (['/login'], LoginApi),
]

for endpoint in endpoints:
    api.add_resource(endpoint[1], *endpoint[0])
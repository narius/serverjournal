from werkzeug.security import generate_password_hash,check_password_hash
from flask_restplus import reqparse, abort, Api, Resource
from flask import session, request, g
from flask_login import login_user, current_user, logout_user
from backend.models.user import User
import json
import logging


class LoginApi(Resource):
    def get(self):
        return json.loads(json.dumps({'return':'get_login',}))

    def post(self):
        logging.info("LoginApi.post")
        data = json.loads(request.data)
        username = data['username']
        password = data['password']
        user = User.query.filter_by(username=username).first()
        if not check_password_hash(user.password,password):
            logging.debug("invalid passowrd")
            return {'code: 401,'
                    'message': "invalid passowrd"}
        logging.debug(user)
        login_user(user)
        g.user = user
        logging.debug(session)
        logging.debug(current_user)
        return 200

    def delete(self):
        logging.info("LoginApi.delete")
        logout_user()
        return 201


from datetime import datetime

from flask import request
from flask_restplus import Resource
from mysql.connector import connect, Error

import utils.settings as settings
from api.restplus import api
from api.serializers import email, user

ns = api.namespace('login', description='Handle users information')

@ns.param('email', 'The User email')
class GetUser(Resource):

    @api.marshal_with(user)
    def get(self, email):
        """
        Return the User object with the input email
        """

        #TODO: implement

        answ = [{
            'email': 'test@cnr.it',
            'name': 'nedo',
            'job': 'student'
        }]

        return answ, 200


@ns.param('email', 'The user email')
@ns.param("name", "The user name")
@ns.param("job", "The user job")
class PostUser(Resource):

    @api.response(200, 'User added')
    def post(self, email, name, job):
        """
        Send (eventually, update) an answer for a specific user.
        """

        # TODO: implement

        return "OK", 200


ns.add_resource(GetUser, '/<string:email>')
ns.add_resource(PostUser, '/<string:email>/<string:name>/<string:job>')

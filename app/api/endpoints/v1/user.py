from datetime import datetime

from flask import request
from flask_restplus import Resource
from mysql.connector import connect, Error

import utils.settings as settings
from api.restplus import api
from api.serializers import email, user
from utils.settings import conn

ns = api.namespace('user', description='Handle users information')

@ns.param('email', 'The User email')
class GetUser(Resource):

    @api.marshal_with(user)
    def get(self, email):
        """
        Return the User object with the input email
        """

        cursor = conn.cursor()
        query = ('SELECT * FROM users WHERE email = %s')
        eml = (email,)
        row_count = cursor.execute(query, eml)

        if row_count != 0:
            rows = cursor.fetchall()
            print("roooooows",rows)
            for row in rows:
                answer = [{
                    'email': row[1],
                    'name': row[2],
                    'job': row[3]
                }]

            return answer, 200
        else:
            return "No user with such email", 404
            cursor.close()



@ns.param('email', 'The user email')
@ns.param("name", "The user name")
@ns.param("job", "The user job")
class PostUser(Resource):

    @api.response(200, 'User added')
    def post(self, email, name, job):
        """
        Send (eventually, update) an answer for a specific user.
        """
        try:
            cur = conn.cursor()
            query2 = ("insert into users (email,name,job) values (%s, %s, %s)")
            pld = (email, name, job,)
            cur.execute(query2, pld)
            print(email, name, job)
            conn.commit()
        except NameError:
            return "Something went wrong"
        finally:
            cur.close()
        return "User added", 200


ns.add_resource(GetUser, '/<string:email>')
ns.add_resource(PostUser, '/<string:email>/<string:name>/<string:job>')

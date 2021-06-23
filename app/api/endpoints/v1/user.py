from datetime import datetime
import mysql.connector as mysql
import pymysql
from flask import request
from flask_restplus import Resource
from mysql.connector import connect, Error

import utils.settings as settings
from api.restplus import api
from api.serializers import email, user

conn = mysql.connect(
    host = "localhost",
    user = "root",
    port = "32000",
    passwd = "admin0x",
    database = "login"
)

ns = api.namespace('user', description='Handle users information')

@ns.param('email', 'The User email')
class GetUser(Resource):

    @api.marshal_with(user)
    def get(self, email):
        """
        Return the User object with the input email
        """

        #TODO: implement

        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = 'SELECT * FROM users'
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == email:
                answ = [{
                    'email': row[1],
                    'name': row[2],
                    'job': row[3]
                }]
                cursor.close()

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
        cur = conn.cursor()
        cur.execute("insert into users (email,name,job) values (%s, %s, %s)", (email, name, job))
        print(email, name, job)
        conn.commit()
        cur.close()
        return "OK", 200


ns.add_resource(GetUser, '/<string:email>')
ns.add_resource(PostUser, '/<string:email>/<string:name>/<string:job>')

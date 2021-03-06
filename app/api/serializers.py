from flask_restplus import fields

from api.restplus import api

email = api.model('user email', {
    'email': fields.String(required=True, example='test@cnr.it',
                          # pattern='',  TODO: implement
                          description='The user email'),
})

user = api.inherit('user', email, {
    'name': fields.String(required=True, description='The name of the user'),
    'job': fields.String(required=True, description='The job of the user')
})

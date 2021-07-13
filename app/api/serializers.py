from flask_restplus import fields

from api.restplus import api

email = api.model('user email', {
    'email': fields.String(required=True, example='test@cnr.it',
                           pattern='\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',
                           #\S+@\S+.\S+
                           description='The user email'),
})

user = api.inherit('user', email, {
    'name': fields.String(required=True, description='The name of the user'),
    'job': fields.String(required=True, description='The job of the user')
})

from flask_restful import Resource
from schemas import SignUpSchema
from models import User
from flask import request

class SignUpAPI(Resource):
    schema = SignUpSchema()

    def post(self):
        #print(request.form)
        args = self.schema.load(request.form)
        #print(args)
        #print(args[0]["username"])
        user = User(username = args.data["username"])
        user.hashPassword(args.data["password"])
        user.save()

        return {'username': user.username}

from flask_restful import Resource
from schemas import SignUpSchema
from flask import g, request, jsonify
from app import api, auth
from models import User

class getAuthToken(Resource):
    schema = SignUpSchema()

    def post(self):
        args = self.schema.load(request.form).data
        user = User.objects(username = args["username"])[0]

        if not user.verifyPassword(args["password"]):
            return {'message':'Username or Password incorrect.'}, 405

        token = user.generateAuthToken()
        return jsonify({'token': token.decode('ascii')})

api.add_resource(getAuthToken, '/login')
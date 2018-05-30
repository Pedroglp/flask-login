from flask_restful import Resource
from app import api, auth

class ProtectedAPI(Resource):

    @auth.login_required
    def get(self):
        return {'result':'shhh secret'}

api.add_resource(ProtectedAPI, '/secret')
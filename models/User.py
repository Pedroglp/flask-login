from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context
from mongoengine import *
from app import auth, app

class User(Document):
    username = StringField(required = True)
    password_hash = StringField(required = True)

    def hashPassword(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verifyPassword(self, password):
        return pwd_context.verify(password, self.password_hash)

    @staticmethod
    @auth.verify_token
    def verifyAuthToken(token):
        s = Serializer(str(app.config['SECRET_KEY']))
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.objects(id = data['userId'])
        return user

    def generateAuthToken(self, expiration = 600):
        s = Serializer(str(app.config['SECRET_KEY']), expires_in = expiration)
        userId = str(self.id)
        return s.dumps({'userId' : userId})
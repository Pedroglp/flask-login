from flask import Flask
from app.settings import *
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#change this depending on your stage level
app.config.from_object(DevelopmentConfig)
db = MongoEngine(app)
api = Api(app)
ma = Marshmallow(app)
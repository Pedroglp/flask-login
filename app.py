from flask import Flask
from settings import *
from resources import ItemResource, ItemsListResource
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#change this depending on your stage level
app.config.from_object(DevelopmentConfig)
db = MongoEngine(app)
api = Api(app)
ma = Marshmallow(app)

api.add_resource(ItemsListResource, '/items')
api.add_resource(ItemResource, '/items/<string:itemId>')

if __name__ == '__main__':
    app.run()

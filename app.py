from flask import Flask
from settings import *
from resources import Items, ItemsList
from flask_restful import Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
#change this depending of your stage level
app.config.from_object(DevelopmentConfig)
db = MongoEngine(app)
api = Api(app)

api.add_resource(ItemsList, '/items')
api.add_resource(Items, '/items/<string:itemId>')

if __name__ == '__main__':
    app.run()

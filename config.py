from flask import Flask, request
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource

#configuring db
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/local'

mongo = PyMongo(app)

api = Api(app)
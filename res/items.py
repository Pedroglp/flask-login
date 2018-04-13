from config import mongo, Resource
from bson.json_util import dumps, loads

class Items(Resource):
    def get(self, itemId):
        items = mongo.db.items
        return {'result': 'Teste'}

class ItemsList(Resource):
    def get(self):
        items = mongo.db.items
        result = dumps(items)
        #check marshamallow
        return {'result': result}

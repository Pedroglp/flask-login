from config import mongo, Resource

class Items(Resource):
    def get(self, itemId):
        return {'result': 'Teste'}

class ItemsList(Resource):
    def get(self):
        return {'result': 'List'}
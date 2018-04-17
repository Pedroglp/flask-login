
from app import api, app
from resources import ItemResource, ItemsListResource

api.add_resource(ItemsListResource, '/items')
api.add_resource(ItemResource, '/items/<string:itemId>')

if __name__ == '__main__':
    app.run()

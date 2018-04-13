from config import app, api
from res import Items, ItemsList
from flask_restful import Api

api.add_resource(ItemsList, '/items')
api.add_resource(Items, '/items/<string:itemId>')

if __name__ == '__main__':
    app.run(debug=True)

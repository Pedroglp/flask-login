
from app import api, app
from resources import ItemResource, ItemsListResource, SignUpAPI, UserAPI, LoginAPI

api.add_resource(SignUpAPI, '/signup')

if __name__ == '__main__':
    app.run()

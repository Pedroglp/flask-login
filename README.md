# flask-backend
Study of Flask as Backend (Rest API) using Mongo as Database System.
For serializing data it will be used Flask-Marshmallow and MongoEngine as DRM.

### Prerequisites

You'll need to install local Mongo Database or connect to one in order to be able to run this example. For instructions access:
https://docs.mongodb.com/manual/installation/

### Installing

First, as always initialize your virtualenv.

```
venv -p python3 myenv
source bin activate myenv
```

```
pip install -r requirements.txt
```

## Deployment

```
python app.py
```

## Built With

* [Flask-MongoEngine](https://github.com/mongodb/mongo-python-driver/) - Mongo DRM
* [Flask-RESTful](https://github.com/flask-restful/flask-restful) - RestApi
* [Flask-Marshmallow](http://flask-marshmallow.readthedocs.io/en/latest/) - Schemas
* [Flask](https://github.com/pallets/flask/tree/master/flask) - Backend


## Authors

* **Pedro Gabriel** - *Initial work* - [pedroglp](https://github.com/pedroglp)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This project is just a study to get used with Flask as Backend and Mongo as Database.
* This projets now aims to build a standard project structure for future projects.


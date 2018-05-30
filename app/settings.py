#Config File

#General Config, mutual to all Stages
class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = ['7Y/-PoGH%uo-xg?2jVYXT]omFy)9dI']

class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {}

class DevelopmentConfig(Config):
    MONGODB_SETTINGS = {
        'db': 'local',
        'host':'mongodb://localhost/local',
        'port': 27017,
    }




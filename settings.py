#Config File

#General Config, mutual to all Stages
class Config(object):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {}

class DevelopmentConfig(Config):
    MONGODB_SETTINGS = {
        'db': 'local',
        'host':'mongodb://localhost/local',
        'port': 27017,
    }




from flask_mongoengine.wtf import model_form
from mongoengine import *

class Owner(EmbeddedDocument):
    id = StringField(required = True)
    name = StringField(required = True)

class Item(Document):
    name = StringField(required = True)
    group = StringField()
    owner = EmbeddedDocumentField(Owner)
    status = StringField()

    #needed if Schema already exists at db
    meta = {
        'collection': 'Items'
    }
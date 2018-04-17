from models import Item
from app import ma

class OwnerSchema(ma.Schema):
    class Meta:
        fields = ('id','name')

class ItemSchema(ma.Schema):
    owner = ma.Nested(OwnerSchema)
    class Meta:
        fields = ('name', 'group','owner')
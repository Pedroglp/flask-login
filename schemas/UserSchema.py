from models import Item
from app import ma

class SignUpSchema(ma.Schema):
    class Meta:
        fields = ('username','password')
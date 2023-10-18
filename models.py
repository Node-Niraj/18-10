from mongoengine import *

class Employee(Document):
    name =StringField(max_length=100)
    age = IntField()
    tech =ListField()
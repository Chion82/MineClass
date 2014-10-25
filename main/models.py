from django.db import models
from mongoengine import *

#Classes to access MongoDB via mongoengine

#Users
class users(Document):
	username = StringField()
	password = StringField()
	email = EmailField()
	priority = IntField()
	realname = StringField()
	birthday = LongField()
	avatar = StringField()
	tag = ListField()
	classindex = IntField()
	introduction = StringField()
	sex = IntField()
	creatingtime = LongField()

class AccessTokens(Document):
	token = StringField()
	expires = LongField()
	username = StringField()

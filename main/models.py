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

#Access Tokens
class AccessTokens(Document):
	token = StringField()
	expires = LongField()
	username = StringField()

#Announcements
class announcements(Document):
	PublishmentTime = LongField()
	announcement = StringField()
	publisher = StringField()
	attachment = StringField()
	tag = ListField()
	classes = ListField()
	ReadUsers = ListField()

#Treehole
class treehole(Document):
	PublishmentTime = LongField()
	treehole = StringField()
	pic = StringField()

#Schedule
class schedule(Document):
    PublishmentTime=LongField()
    publisher=StringField()
    title=StringField()
    introduction=StringField()
    classes = ListField()
    startdate=LongField()
    enddate=LongField()

#Class Info
class classinfo(Document):
	classindex = IntField()
	classname = StringField()
	major = StringField()
	period = StringField()

class comments(Document):
	CommentType = IntField()  #0:Announcements, 1:Treeholes
	comment = StringField()
	publisher = StringField()
	PublishmentTime = LongField()
	objid = StringField()

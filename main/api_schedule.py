from main.models import *
from main.escape import *
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mongoengine import *
import random
from main.api_users import *

#API_CreateEvent(request) Create an event in schedule
#Input parameters: HttpRequest Object : POST data
#Return value: HttpResponse Object
def API_CreateEvent(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"AccessToken invalid. Please login first."}',{})
	if (request.POST.get("title")==None or request.POST.get("title")==''):
		return HttpResponse('{"code":1,"message":"Empty title."}',{})
	if (request.POST.get("introduction")==None or request.POST.get("introduction")==''):
		return HttpResponse('{"code":1,"message":"Empty introduction."}',{})
	if (request.POST.get("startdate")==None):
		return HttpResponse('{"code":1,"message":"Empty start date."}',{})
	if (request.POST.get("enddate")==None):
		return HttpResponse('{"code":1,"message":"Empty end date."}',{})
	if (request.POST.get("startdate")>request.POST.get("enddate")):
		return HttpResponse('{"code":1,"message":"start date>end date."}',{})
	dbobj=schedule()
	dbobj.PublishmentTime=int(time.time())
	dbobj.introduction=QuoteContent(request.POST.get("introduction"))
	dbobj.title=QuoteContent(request.POST.get("title"))
	dbobj.publisher=GetUsernameByToken(request.COOKIES.get("accesstoken"))
	dbobj.startdate=request.POST.get("startdate")
	dbobj.enddate=request.POST.get("enddate")

	classes=[]
	username = GetUsernameByToken(request.COOKIES.get("accesstoken"))
	userobj = users.objects(username=username).first()
	if (userobj.priority<=1):
		classes.append(userobj.classindex)
	else:
		if (len(request.POST.getlist('class[]'))>0):
			for classindex in request.POST.getlist('class[]'):
				classes.append(classindex)
		else:
			classes.append(userobj.classindex)
	dbobj.classes=classes

	dbobj.save()
	return HttpResponse('{"code":2,"message":"Success."}')


#API_GetEvent(request) Get list of events in required time
#Input parameters: HttpRequest Object : GET data
#Return value: HttpResponse Object
def API_GetEvent(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"AccessToken invalid. Please login first."}',{})
	username=GetUsernameByToken(request.COOKIES.get("accesstoken"))
	userclass=users.objects(username=username).first().classindex
	input_startdate=request.POST.get("startdate")
	input_enddate=request.POST.get("enddate")

	dbobj=schedule.objects(classes=userclass).order_by("-PublishmentTime").all()
	eventlist=[]
	for RowObj in dbobj:
		if (input_startdate<=RowObj.enddate or Rowobj.startdate<=input_enddate):
			eventlist.append(eval(RowObj.to_json()))

	return HttpResponse(json.dumps(eventlist),{})


#API_DeleteEvent(request) Delete an event specified by id
#Input parameters: HttpRequest Object : GET data
#Return value: HttpResponse Object
def API_DeleteEvent(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"Please login first."}')
	if (request.GET.get("id")==None or request.GET.get("id")==""):
		return HttpResponse('{"code":1,"message":"Invalid input"}')
	username = GetUsernameByToken(request.COOKIES.get("accesstoken"))
	userobj = users.objects(username=username).first()
	userclass = userobj.classindex
	userpriority = userobj.priority
	eventobj= schedule.objects(id=request.GET.get("id"))

	if (eventobj.count()==0):
		return HttpResponse('{"code":2,"message":"Invalid id"}')
	if (userpriority==0 and username!=eventobj.first().publisher):
		return HttpResponse('{"code":3,"message":"Permission denied."}')

	if (userpriority<=1):
		classlist = eventobj.first().classes
		index = 0
		for SingleClass in classlist:
			if (SingleClass==userclass):
				del classlist[index]
				break
			index+=1
		eventobj.update(set__classes=classlist)
	elif (userpriority>=2):
		eventobj.delete()
	return HttpResponse('{"code":4,"message":"Success in deleting event."}')

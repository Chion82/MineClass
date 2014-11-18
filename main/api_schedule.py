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

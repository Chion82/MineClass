from main.models import *
from main.escape import *
from main.api_users import *
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mongoengine import *

def API_CreateClass(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"Invalid Token."}',{})
	if (GetUserPriorityByRequest(request)<2):
		return HttpResponse('{"code":1,"message":"Permission denied."}',{})		
	input_classindex = request.POST.get("classindex")
	input_major = QuoteEscapeContent(request.POST.get("major"))
	input_classname = QuoteEscapeContent(request.POST.get("classname"))
	input_period = QuoteEscapeContent(request.POST.get("period"))
	if (input_classname==None or input_classname=="" or input_classindex==None or input_classindex=="" or input_major==None or input_major=="" or input_period==None or input_period==""):
		return HttpResponse('{"code":2,"message":"Invalid Input."}',{})
	if (classinfo.objects(classindex=input_classindex).count()>0):
		return HttpResponse('{"code":3,"message":"Class Index exists."}',{})
	dbobj = classinfo()
	dbobj.classindex = int(input_classindex)
	dbobj.classname = input_classname
	dbobj.major = input_major
	dbobj.period = input_period
	dbobj.save()
	return HttpResponse('{"code":4,"message":"Success."}',{})

def API_GetClassInfoByIndex(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"Invalid Token."}',{})
	query_index = request.GET.get("classindex")
	if (query_index==None or query_index==""):
		return HttpResponse('{"code":1,"message":"Invalid Input."}',{})
	result = classinfo.objects(classindex=query_index)
	if (result.count()==0):
		return HttpResponse('{"code":2,"message":"Class doesn\'t exit"}')
	return HttpResponse('{"code":3,"message":"Success.","ClassInfo": %s}' % result.first().to_json(),{})

def API_GetAllClassInfo(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"Invalid Token."}',{})
	dbobj = classinfo.objects().all()
	return HttpResponse('{"code":1,"message":"Success.","ClassInfo": %s}' % dbobj.to_json(),{})

def API_DeleteClassByIndex(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"Invalid Token."}',{})
	if (GetUserPriorityByRequest(request)<3):
		return HttpResponse('{"code":1,"message":"Permission denied."}',{})
	query_index = request.GET.get("classindex")
	if (query_index==None or query_index==""):
		return HttpResponse('{"code":2,"message":"Invalid Input."}',{})
	result = classinfo.objects(classindex=int(query_index))
	if (result.count()==0):
		return HttpResponse('{"code":3,"message":"Class doesn\'t exit"}')
	result.delete()
	return HttpResponse('{"code":4,"message":"Success."}',{})
	
from main.models import *
from main.escape import *
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mongoengine import *
import random
from main.api_users import *

def API_PublishComment(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"Invalid AccessToken."}',{})
	input_CommentType = QuoteEscapeContent(request.POST.get("commenttype"))
	input_comment = QuoteEscapeContent(request.POST.get("comment"))
	input_publisher = GetUsernameByRequest(request)
	input_id = QuoteEscapeContent(request.POST.get("id"))
	input_PublishmentTime = int(time.time())
	if (input_CommentType==None or input_CommentType=="" or input_comment==None or input_comment=="" or input_publisher==None or input_publisher==""):
		return HttpResponse('{"code":1,"message":"Invalid Input"}',{})
	if (input_CommentType=="0"):
		dbobj = announcements.objects(id=input_id)
	else:
		dbobj = treehole.objects(id=input_id)
	if (dbobj.count()==0):
		return HttpResponse('{"code":2,"message":"Invalid ID."}',{})
	comobj = comments()
	comobj.CommentType = int(input_CommentType)
	comobj.comment = input_comment
	comobj.publisher = input_publisher
	comobj.PublishmentTime = input_PublishmentTime
	comobj.objid = input_id
	comobj.save()
	return HttpResponse('{"code":3,"message":"Success."}',{})

def API_GetCommentsByID(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"Invalid AccessToken."}',{})
	input_id = request.GET.get("id")
	input_CommentType = request.GET.get("commenttype")
	if (input_id==None or input_id=="" or input_CommentType==None or input_CommentType==""):
		return HttpResponse('{"code":1,"message":"Invalid Input."}',{})
	dbobj = comments.objects(objid=input_id,CommentType=int(input_CommentType))
	return HttpResponse('{"code":3,"message":"Success.","comments": %s}' % dbobj.all().to_json(),{})

def API_DeleteCommentByID(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"Invalid AccessToken."}',{})
	if (GetUserPriorityByRequest(request)<2):
		return HttpResponse('{"code":2,"message":"Permission Denied."}',{})
	input_id = request.GET.get("id")
	if (input_id==None or input_id==""):
		return HttpResponse('{"code":1,"message":"Invalid Input."}',{})
	dbobj = comments.objects(id=input_id)
	if (dbobj.count()==0):
		return HttpResponse('{"code":3,"message":"Invalid ID"}',{})
	dbobj.delete()
	return HttpResponse('{"code":4,"message":"Success."}',{})

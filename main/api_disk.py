from main.models import *
from main.escape import *
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mongoengine import *
import random
from main.api_users import *
import json

def API_AddFile(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"AccessToken invalid. Please login first."}',{})
	input_FileName = QuoteEscapeContent(request.POST.get("filename"))
	input_folder = QuoteEscapeContent(request.POST.get("folder"))
	input_URL = QuoteEscapeContent(request.POST.get("url"))
	if (input_FileName==None or input_FileName=="" or input_folder==None or input_folder=="" or input_URL==None or input_URL==""):
		return HttpResponse('{"code":1,"message":"Invalid Input."}',{})
	if(disk.objects(folder=input_folder,FileName="$FOLDER$").count()==0):
		return HttpResponse('{"code":2,"message":"Folder doesn\'t exist"}',{})
	if(disk.objects(folder=input_folder,FileName=input_FileName).count()!=0):
		return HttpResponse('{"code":3,"message":"File exists."}',{})
	dbobj = disk()
	dbobj.FileName = input_FileName
	dbobj.folder = input_folder
	dbobj.URL = input_URL
	dbobj.uploader = GetUsernameByRequest(request)
	dbobj.save()
	return HttpResponse('{"code":4,"message":"Success."}',{})

def API_ExploreFolder(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"AccessToken invalid. Please login first."}',{})
	input_folder = QuoteEscapeContent(request.GET.get("folder"))
	if (input_folder==None or input_folder==""):
		return HttpResponse('{"code":1,"message":"Invalid Input."}',{})
	if (disk.objects(folder=input_folder,FileName="$FOLDER$").count()==0):
		return HttpResponse('{"code":2,"message":"Folder doesn\'t exist"}',{})
	dbobj = disk.objects(folder=input_folder,FileName__ne="$FOLDER$")
	files = dbobj.all().to_json()
	SubFolderQuery = disk.objects(FileName="$FOLDER$",folder__startswith=input_folder)
	SubFolderList = []
	for SubFolder in SubFolderQuery:
		if (SubFolder.folder.count(QuoteEscapeContent("/"))==input_folder.count(QuoteEscapeContent("/"))+1 and SubFolder.folder!=input_folder):
			SubFolderList.append(SubFolder)
	return HttpResponse('{"code":3,"message":"Success","files":%s,"folders":%s}' % (files,json.dumps(SubFolderList)),{})

def API_CreateFolder(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"AccessToken invalid. Please login first."}',{})
	input_folder = QuoteEscapeContent(request.GET.get("folder"))
	if (input_folder==None or input_folder==""):
		return HttpResponse('{"code":1,"message":"Invalid Input."}',{})
	if(disk.objects(folder=input_folder,FileName="$FOLDER$").count()!=0):
		return HttpResponse('{"code":2,"message":"Folder exists"}',{})
	dbobj = disk()
	dbobj.FileName = "$FOLDER$"
	dbobj.folder = input_folder
	dbobj.URL = ""
	dbobj.uploader = GetUsernameByRequest(request)
	dbobj.save()
	return HttpResponse('{"code":3,"message":"Success."}',{})

def API_DeleteFileOrFolder(request):
	if (not VerifyToken(request)):
		return HttpResponse('{"code":0,"message":"AccessToken invalid. Please login first."}',{})
	input_FileName = QuoteEscapeContent(request.GET.get("filename"))
	input_folder = QuoteEscapeContent(request.GET.get("folder"))
	input_IsFolder = request.GET.get("isfolder")
	if (input_IsFolder==None or input_IsFolder==""):
		return HttpResponse('{"code":1,"message":"Invalid Input."}',{})
	if (input_IsFolder=="0"):
		if (input_FileName==None or input_FileName=="" or input_folder==None or input_folder==""):
			return HttpResponse('{"code":1,"message":"Invalid Input."}',{})
		dbobj = disk.objects(FileName=input_FileName,folder=input_folder)
	else:
		if (input_folder==None or input_folder==""):
			return HttpResponse('{"code":1,"message":"Invalid Input."}',{})
		dbobj = disk.objects(FileName="$FOLDER$",folder=input_folder)
	if (dbobj.count()==0):
		return HttpResponse('{"code":2,"message":"Folder or file doesn\'t exist"}',{})
	if (GetUserPriorityByRequest(request)<2 and dbobj.first().uploader!=GetUsernameByRequest(request)):
		return HttpResponse('{"code":3,"message":"Permission Denied."}',{})
	dbobj.delete()
	return HttpResponse('{"code":4,"message":"Success."}',{})

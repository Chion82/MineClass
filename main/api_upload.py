from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import time
import random
import os
from main.config import *

def API_UploadFile(request):
	if (request.FILES.get("file")==None):
		return HttpResponse('{"code":0,"message":"Invalid Input."}', {})

	FileObj = request.FILES.get("file")
	FileNameArr = FileObj.name.split(".")
	if (len(FileNameArr)>0):
		FileType = FileNameArr[len(FileNameArr)-1]
	else:
		FileType = ""

	if (not FileType in ALLOWEDFILETYPES):
		return HttpResponse('{"code":1,"message":"Unsupported file type."}', {})

	path =  "static/upload/" + ("%d" % int(time.time())) + ("%d" % random.randint(100000,999999)) + '.' + FileType
	while (os.path.exists(os.path.split(os.path.realpath(__file__))[0] + "/" + path)):
		path = "static/upload/" + ("%d" % int(time.time())) + ("%d" % random.randint(100000,999999)) + '.' + FileType
	dest = open(os.path.split(os.path.realpath(__file__))[0] + "/" + path,'wb+')
	dest.write(FileObj.read())
	dest.close()
	return HttpResponse('{"code":2,"message":"Success.","path":"%s"}' % path, {})

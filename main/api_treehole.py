from main.models import *
from main.escape import *
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mongoengine import *
import random
import pycurl

def API_PublishTreehole(request):
	if (request.POST.get("treehole")==None):
		return HttpResponse('{"code":0,"message":"Empty treehole content."}')
	curl = pycurl.Curl()
	dbobj = treehole()
	dbobj.PublishmentTime = int(time.time())
	dbobj.treehole = QuoteContent(request.POST.get("treehole"))
	if (request.POST.get("pic")==None or request.POST.get("pic")=="none" or request.POST.get("pic")==""):
		dbobj.pic = "none"
		curl.setopt(curl.URL,"https://api.weibo.com/2/statuses/update.json")
		curl.setopt(curl.POST,True)
		curl.setopt(curl.POSTFIELDS,'access_token=' + WEIBOACCESSTOKEN + '&status=' + QuoteContent(request.POST.get("treehole")))
		curl.perform()
		curl.close()
	else:
		dbobj.pic = request.POST.get("pic")
		curl.setopt(curl.URL,"https://upload.api.weibo.com/2/statuses/upload.json")
		curl.setopt(curl.POST,True)
		curl.setopt(curl.HTTPPOST,[('access_token',(curl.FORM_CONTENTS,WEIBOACCESSTOKEN)), ('status',(curl.FORM_CONTENTS,QuoteContent(request.POST.get("treehole")))), ('pic',(curl.FORM_FILE,request.POST.get("pic")))])
		curl.perform()
		curl.close()
	dbobj.save()
	return HttpResponse('{"code":1,"message":"Success."}',{})

def API_GetTreehole(request):
	dbobj = treehole.objects().order_by('-PublishmentTime').all()
	TreeholeList = []
	for row in dbobj:
		TreeholeList.append(row.to_json())
	return HttpResponse(str(TreeholeList),{})

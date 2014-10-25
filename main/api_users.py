<<<<<<< HEAD
from main.models import *
from main.escape import *
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mongoengine import *
import random

#API_CreateUser(request)  [web API function] Create an user
#input paramaters: HttpRequst object: POST data
#return value: HttpResponse object: JSON result of creating an user
def API_CreateUser(request):
	input_username = QuoteEscapeContent(request.POST.get("username"))
	input_password = QuoteEscapeContent(request.POST.get("password"))
	input_email = EscapeContent(request.POST.get("email"))
	input_priority = 0
	input_realname = QuoteEscapeContent(request.POST.get("realname"))
	input_birthday = -1
	input_avatar = "static/upload/avatars/none.png"
	input_tag = []
	if (request.POST.get("classindex")!=None):
		input_classindex = int(request.POST.get("classindex"))
	else:
		input_classindex = None
	input_introduction = ""
	if (request.POST.get("sex")!=None):
		input_sex = int(request.POST.get("sex"))
	else:
		input_sex = None
	input_creatingtime = time.time()
	if (input_username==None or input_password==None or input_email==None or input_realname==None
		or input_classindex==None or input_sex==None):
		return HttpResponse('{"code":0,"message":"Invalid paramaters."}',{})
	if (users.objects(username=input_username).count()>0):
		return HttpResponse('{"code":1,"message":"Username exists."}',{})
	if (users.objects(email=input_email).count()>0):
		return HttpResponse('{"code":2,"message":"Email exists."}',{})
	dbobj = users()
	dbobj.username = input_username
	dbobj.password = md5(input_password)
	dbobj.email = input_email
	dbobj.priority = input_priority
	dbobj.realname = input_realname
	dbobj.birthday = input_birthday
	dbobj.avatar = input_avatar
	dbobj.tag = input_tag
	dbobj.classindex = input_classindex
	dbobj.introduction = input_introduction
	dbobj.sex = input_sex
	dbobj.creatingtime = input_creatingtime
	dbobj.save()
	return HttpResponse('{"code":3,"message":"User created."}',{})

#API_UpdateSelfInfo(request) [web API function] Update the information of the user binded with the given token
#input parameters: HttpRequest Object: COOKIE(token)(required) POST data (optional)
#return value: HttpResponse Object: JSON Result of updating user details
def API_UpdateSelfInfo(request):
	AccessToken = request.COOKIES.get("accesstoken")
	if (not IsTokenValid(AccessToken)):
		return HttpResponse('{"code":0,"message":"Token invalid."}',{})
	username = GetUsernameByToken(AccessToken)
	input_email = EscapeContent(request.POST.get("email"))
	input_realname = QuoteEscapeContent(request.POST.get("realname"))
	if (request.POST.get("birthday")!=None):
		input_birthday = int(request.POST.get("birthday"))
	else:
		input_birthday = None
	input_avatar = EscapeContent(request.POST.get("avatar"))
	
	if (len(request.POST.getlist("tag[]"))>0):
		input_tag = []
		for SingleTag in request.POST.getlist("tag[]"):
			input_tag.append(QuoteEscapeContent(SingleTag))
	else:
		input_tag = None
	if (request.POST.get("classindex")!=None):
		input_classindex = int(request.POST.get("classindex"))
	else:
		input_classindex = None
	input_introduction = QuoteEscapeContent(request.POST.get("introduction"))
	if (request.POST.get("sex")!=None):
		input_sex = int(request.POST.get("sex"))
	else:
		input_sex = None
	UpdateUserInfo(username,email=input_email,realname=input_realname,birthday=input_birthday,avatar=input_avatar,tag=input_tag,classindex=input_classindex,introduction=input_introduction,sex=input_sex)
	return HttpResponse('{"code":1,"message":"Update completed."}')


#API_Login(request) [web API function] login by the given username and password
#input parameters: HttpRequest Object: POST data
#return value: HttpResponse Object: JSON Result of login
def API_Login(request):
	input_username = QuoteEscapeContent(request.POST.get("username"))
	input_password = QuoteEscapeContent(request.POST.get("password"))
	dbobj = users.objects(username=input_username)
	if (dbobj.count()==0):
		return HttpResponse('{"code":0,"message":"No such user."}',{})
	if (dbobj.first().password!=md5(input_password)):
		return HttpResponse('{"code":1,"message":"Password incorrect."}',{})
	token = md5(str(time.time()) + str(random.randint(100000,999999)))
	dbobj = AccessTokens()
	dbobj.token = token
	dbobj.expires = time.time()+30*24*60*60
	dbobj.username = input_username
	dbobj.save()
	response = HttpResponse('{"code":2,"message":"Success.","token":"' + token + '"}',{})
	response.set_cookie("accesstoken",token,max_age=30*24*60*60,path="/")
	return response

#API_Logout(request) [web API function] logout by the given token
#input parameters: HttpRequest Object: COOKIE(token)
#return value: HttpResponse Object: JSON result
def API_Logout(request):
	AccessToken = request.COOKIES.get("accesstoken")
	if (not IsTokenValid(AccessToken)):
		return HttpResponse('{"code":0,"message":"Token invalid."}',{})
	AccessTokens.objects(token=AccessToken).delete()
	response = HttpResponse('{"code":1,"message":"Success."}',{})
	response.delete_cookie("accesstoken",path="/")
	return response

#API_GetUserInfo(request) [web API function] Retrieve user information by the given token
#input parameters: HttpRequest Object: COOKIE(token)
#return value: HttpResponse Object: JSON result
def API_GetUserInfo(request):
	AccessToken = request.COOKIES.get("accesstoken")
	if (not IsTokenValid(AccessToken)):
		return HttpResponse('{"code":0,"message":"Token invalid."}',{})
	username = GetUsernameByToken(AccessToken)
	dbobj = users.objects(username=username)
	JSONResult = dbobj.first().to_json()
	return HttpResponse('{"code":1,"message":"Success.","UserInfo":'+ JSONResult +'}',{})

#API_GetUserInfoByUsername(request) [web API function] Retrieve user information by the given username
#input parameters: HttpRequest Object: COOKIE(token),POST(username[])
#return value: HttpResponse Object: JSON result
def API_GetUserInfoByUsername(request):
	AccessToken = request.COOKIES.get("accesstoken")
	if (not IsTokenValid(AccessToken)):
		return HttpResponse('{"code":0,"message":"Token invalid."}',{})
	if (not len(request.POST.getlist("username[]"))>0):
		return HttpResponse('{"code":0,"message":"Username array invalid."}',{})
	UsernameList = request.POST.getlist("username[]")
	JSONResult = []
	for username in UsernameList:
		dbobj = users.objects(username=username)
		if (not dbobj.count()>0):
			JSONResult.append({"error":1,"message":"No such user."})
			continue
		raw = eval(dbobj.first().to_json())
		del raw["password"]
		JSONResult.append(raw)
	return HttpResponse('{"code":1,"message":"Success.","UserInfo":'+ str(JSONResult) +'}',{})


#IsTokenValid(token) To verify valid token
#input parameters: String token
#return value: 1-token valid, 0-token Invalid
def IsTokenValid(token):
	if (token==None):
		return 0
	dbobj = AccessTokens.objects(token=token)
	if (dbobj.count()==0):
		return 0
	if (dbobj.first().expires<time.time()):
		return 0
	return 1

#GetUsernameByToken(token) To get the username by passing valid token
#input parameters: String token
#return value: String username if token valid, None if token Invalid
def GetUsernameByToken(token):
	if (not IsTokenValid(token)):
		return None
	dbobj = AccessTokens.objects(token=token).first()
	return dbobj.username

#UpdateUserInfo(username,**option) To update user infomation by passing username and options
#input parameters: String username, **option
#return value: None
def UpdateUserInfo(username,**option):
	if(option.has_key('email')):
		input_email = option['email']
	else:
		input_email = None

	if(option.has_key('priority')):
		input_priority = option['priority']
	else:
		input_priority = None

	if(option.has_key('realname')):
		input_realname = option['realname']
	else:
		input_realname = None

	if(option.has_key('birthday')):
		input_birthday = option['birthday']
	else:
		input_birthday = None

	if(option.has_key('avatar')):
		input_avatar = option['avatar']
	else:
		input_avatar = None

	if(option.has_key('tag')):
		input_tag = option['tag']
	else:
		input_tag = None

	if(option.has_key('classindex')):
		input_classindex = option['classindex']
	else:
		input_classindex = None

	if(option.has_key('introduction')):
		input_introduction = option['introduction']
	else:
		input_introduction = None

	if(option.has_key('sex')):
		input_sex = option['sex']
	else:
		input_sex = None
	
	dbobj = users.objects(username=username)
	if(input_email!=None):
		dbobj.update(set__email=input_email)
	if(input_priority!=None):
		dbobj.update(set__priority=input_priority)
	if(input_realname!=None):
		dbobj.update(set__realname=input_realname)
	if(input_birthday!=None):
		dbobj.update(set__birthday=input_birthday)
	if(input_avatar!=None):
		dbobj.update(set__avatar=input_avatar)
	if(input_tag!=None):
		dbobj.update(set__tag=input_tag)
	if(input_classindex!=None):
		dbobj.update(set__classindex=input_classindex)
	if(input_introduction!=None):
		dbobj.update(set__introduction=input_introduction)
	if(input_sex!=None):
		dbobj.update(set__sex=input_sex)
=======
from main.models import *
from main.escape import *
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mongoengine import *
import random

#API_CreateUser(request)  [web API function] Create an user
#input paramaters: HttpRequst object: POST data
#return value: HttpResponse object: JSON result of creating an user
def API_CreateUser(request):
	input_username = QuoteEscapeContent(request.POST.get("username"))
	input_password = QuoteEscapeContent(request.POST.get("password"))
	input_email = EscapeContent(request.POST.get("email"))
	input_priority = 0
	input_realname = QuoteEscapeContent(request.POST.get("realname"))
	input_birthday = -1
	input_avatar = "static/upload/avatars/none.png"
	input_tag = []
	if (request.POST.get("classindex")!=None):
		input_classindex = int(request.POST.get("classindex"))
	else:
		input_classindex = None
	input_introduction = ""
	if (request.POST.get("sex")!=None):
		input_sex = int(request.POST.get("sex"))
	else:
		input_sex = None
	input_creatingtime = time.time()
	if (input_username==None or input_password==None or input_email==None or input_realname==None
		or input_classindex==None or input_sex==None):
		return HttpResponse('{"code":0,"message":"Invalid paramaters."}',{})
	if (users.objects(username=input_username).count()>0):
		return HttpResponse('{"code":1,"message":"Username exists."}',{})
	if (users.objects(email=input_email).count()>0):
		return HttpResponse('{"code":2,"message":"Email exists."}',{})
	dbobj = users()
	dbobj.username = input_username
	dbobj.password = md5(input_password)
	dbobj.email = input_email
	dbobj.priority = input_priority
	dbobj.realname = input_realname
	dbobj.birthday = input_birthday
	dbobj.avatar = input_avatar
	dbobj.tag = input_tag
	dbobj.classindex = input_classindex
	dbobj.introduction = input_introduction
	dbobj.sex = input_sex
	dbobj.creatingtime = input_creatingtime
	dbobj.save()
	return HttpResponse('{"code":3,"message":"User created."}',{})

#API_UpdateSelfInfo(request) [web API function] Update the information of the user binded with the given token
#input parameters: HttpRequest Object: COOKIE(token)(required) POST data (optional)
#return value: HttpResponse Object: JSON Result of updating user details
def API_UpdateSelfInfo(request):
	AccessToken = request.COOKIES.get("accesstoken")
	if (not IsTokenValid(AccessToken)):
		return HttpResponse('{"code":0,"message":"Token invalid."}',{})
	username = GetUsernameByToken(AccessToken)
	input_email = EscapeContent(request.POST.get("email"))
	input_realname = QuoteEscapeContent(request.POST.get("realname"))
	if (request.POST.get("birthday")!=None):
		input_birthday = int(request.POST.get("birthday"))
	else:
		input_birthday = None
	input_avatar = EscapeContent(request.POST.get("avatar"))
	
	if (len(request.POST.getlist("tag[]"))>0):
		input_tag = []
		for SingleTag in request.POST.getlist("tag[]"):
			input_tag.append(QuoteEscapeContent(SingleTag))
	else:
		input_tag = None
	if (request.POST.get("classindex")!=None):
		input_classindex = int(request.POST.get("classindex"))
	else:
		input_classindex = None
	input_introduction = QuoteEscapeContent(request.POST.get("introduction"))
	if (request.POST.get("sex")!=None):
		input_sex = int(request.POST.get("sex"))
	else:
		input_sex = None
	UpdateUserInfo(username,email=input_email,realname=input_realname,birthday=input_birthday,avatar=input_avatar,tag=input_tag,classindex=input_classindex,introduction=input_introduction,sex=input_sex)
	return HttpResponse('{"code":1,"message":"Update completed."}')


#API_Login(request) [web API function] login by the given username and password
#input parameters: HttpRequest Object: POST data
#return value: HttpResponse Object: JSON Result of login
def API_Login(request):
	input_username = QuoteEscapeContent(request.POST.get("username"))
	input_password = QuoteEscapeContent(request.POST.get("password"))
	dbobj = users.objects(username=input_username)
	if (dbobj.count()==0):
		return HttpResponse('{"code":0,"message":"No such user."}',{})
	if (dbobj.first().password!=md5(input_password)):
		return HttpResponse('{"code":1,"message":"Password incorrect."}',{})
	token = md5(str(time.time()) + str(random.randint(100000,999999)))
	dbobj = AccessTokens()
	dbobj.token = token
	dbobj.expires = time.time()+30*24*60*60
	dbobj.username = input_username
	dbobj.save()
	response = HttpResponse('{"code":2,"message":"Success.","token":"' + token + '"}',{})
	response.set_cookie("accesstoken",token,max_age=30*24*60*60,path="/")
	return response

#API_Logout(request) [web API function] logout by the given token
#input parameters: HttpRequest Object: COOKIE(token)
#return value: HttpResponse Object: JSON result
def API_Logout(request):
	AccessToken = request.COOKIES.get("accesstoken")
	if (not IsTokenValid(AccessToken)):
		return HttpResponse('{"code":0,"message":"Token invalid."}',{})
	AccessTokens.objects(token=AccessToken).delete()
	response = HttpResponse('{"code":1,"message":"Success."}',{})
	response.delete_cookie("accesstoken",path="/")
	return response

#API_GetUserInfo(request) [web API function] Retrieve user information by the given token
#input parameters: HttpRequest Object: COOKIE(token)
#return value: HttpResponse Object: JSON result
def API_GetUserInfo(request):
	AccessToken = request.COOKIES.get("accesstoken")
	if (not IsTokenValid(AccessToken)):
		return HttpResponse('{"code":0,"message":"Token invalid."}',{})
	username = GetUsernameByToken(AccessToken)
	dbobj = users.objects(username=username)
	JSONResult = dbobj.first().to_json()
	return HttpResponse('{"code":1,"message":"Success.","UserInfo":'+ JSONResult +'}',{})

#API_GetUserInfoByUsername(request) [web API function] Retrieve user information by the given username
#input parameters: HttpRequest Object: COOKIE(token),POST(username[])
#return value: HttpResponse Object: JSON result
def API_GetUserInfoByUsername(request):
	AccessToken = request.COOKIES.get("accesstoken")
	if (not IsTokenValid(AccessToken)):
		return HttpResponse('{"code":0,"message":"Token invalid."}',{})
	if (not len(request.POST.getlist("username[]"))>0):
		return HttpResponse('{"code":0,"message":"Username array invalid."}',{})
	UsernameList = request.POST.getlist("username[]")
	JSONResult = []
	for username in UsernameList:
		dbobj = users.objects(username=username)
		if (not dbobj.count()>0):
			JSONResult.append({"error":1,"message":"No such user."})
			continue
		raw = eval(dbobj.first().to_json())
		del raw["password"]
		JSONResult.append(raw)
	return HttpResponse('{"code":1,"message":"Success.","UserInfo":'+ str(JSONResult) +'}',{})


#IsTokenValid(token) To verify valid token
#input parameters: String token
#return value: 1-token valid, 0-token Invalid
def IsTokenValid(token):
	if (token==None):
		return 0
	dbobj = AccessTokens.objects(token=token)
	if (dbobj.count()==0):
		return 0
	if (dbobj.first().expires<time.time()):
		return 0
	return 1

#GetUsernameByToken(token) To get the username by passing valid token
#input parameters: String token
#return value: String username if token valid, None if token Invalid
def GetUsernameByToken(token):
	if (not IsTokenValid(token)):
		return None
	dbobj = AccessTokens.objects(token=token).first()
	return dbobj.username

#UpdateUserInfo(username,**option) To update user infomation by passing username and options
#input parameters: String username, **option
#return value: None
def UpdateUserInfo(username,**option):
	if(option.has_key('email')):
		input_email = option['email']
	else:
		input_email = None

	if(option.has_key('priority')):
		input_priority = option['priority']
	else:
		input_priority = None

	if(option.has_key('realname')):
		input_realname = option['realname']
	else:
		input_realname = None

	if(option.has_key('birthday')):
		input_birthday = option['birthday']
	else:
		input_birthday = None

	if(option.has_key('avatar')):
		input_avatar = option['avatar']
	else:
		input_avatar = None

	if(option.has_key('tag')):
		input_tag = option['tag']
	else:
		input_tag = None

	if(option.has_key('classindex')):
		input_classindex = option['classindex']
	else:
		input_classindex = None

	if(option.has_key('introduction')):
		input_introduction = option['introduction']
	else:
		input_introduction = None

	if(option.has_key('sex')):
		input_sex = option['sex']
	else:
		input_sex = None
	
	dbobj = users.objects(username=username)
	if(input_email!=None):
		dbobj.update(set__email=input_email)
	if(input_priority!=None):
		dbobj.update(set__priority=input_priority)
	if(input_realname!=None):
		dbobj.update(set__realname=input_realname)
	if(input_birthday!=None):
		dbobj.update(set__birthday=input_birthday)
	if(input_avatar!=None):
		dbobj.update(set__avatar=input_avatar)
	if(input_tag!=None):
		dbobj.update(set__tag=input_tag)
	if(input_classindex!=None):
		dbobj.update(set__classindex=input_classindex)
	if(input_introduction!=None):
		dbobj.update(set__introduction=input_introduction)
	if(input_sex!=None):
		dbobj.update(set__sex=input_sex)
>>>>>>> 62eaae239e1b1b1771d0813d39f397efa0fdca60

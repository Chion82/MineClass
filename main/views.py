from django.shortcuts import render
from django.shortcuts import render_to_response
from main.api_users import *
from django.views.decorators.csrf import csrf_exempt
from main.api_announcements import *
from main.api_upload import *
from main.api_treehole import *

@csrf_exempt
def Render_API_CreateUser(request):
	return API_CreateUser(request)

@csrf_exempt
def Render_API_UpdateSelfInfo(request):
	return API_UpdateSelfInfo(request)

@csrf_exempt
def Render_API_Login(request):
	return API_Login(request)

@csrf_exempt
def Render_API_Logout(request):
	return API_Logout(request)

@csrf_exempt
def Render_API_GetUserInfo(request):
	return API_GetUserInfo(request)

@csrf_exempt
def Render_API_GetUserInfoByUsername(request):
	return API_GetUserInfoByUsername(request)

#Add HTML file
def Render_APITest(request):
	return render_to_response("apitest.html",{})
def Render_Index(request):
	return render_to_response("home_page.html",{})
def Render_SetInfo(request):
	return render_to_response("setinfo.html",{})
def Render_SetHead(request):
	return render_to_response("sethead.html",{})
def Render_SetPassword(request):
	return render_to_response("setpassword.html",{})

@csrf_exempt
def Render_API_PublishAnnouncement(request):
	return API_PublishAnnouncement(request)

def Render_API_GetAnnouncements(request):
	return API_GetAnnouncements(request)

def Render_API_DeleteAnnouncement(request):
	return API_DeleteAnnouncement(request)

@csrf_exempt
def Render_API_UploadFile(request):
	return API_UploadFile(request)

@csrf_exempt
def Render_API_PublishTreehole(request):
	return API_PublishTreehole(request)

def Render_API_GetTreehole(request):
	return API_GetTreehole(request)

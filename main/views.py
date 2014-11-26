from django.shortcuts import render
from django.shortcuts import render_to_response
from main.api_users import *
from django.views.decorators.csrf import csrf_exempt
from main.api_announcements import *
from main.api_upload import *
from main.api_treehole import *
from main.api_schedule import *
from main.api_classinfo import *
from main.api_comments import *
from main.api_disk import *

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
def Render_Inform(request):
	return render_to_response("inform.html",{})
def Render_Discuss(request):
	return render_to_response("discuss.html",{})
def Render_Login(request):
	return render_to_response("login.html",{})
def Render_Regist(request):
	return render_to_response("regist.html",{})

@csrf_exempt
def Render_API_PublishAnnouncement(request):
	return API_PublishAnnouncement(request)

def Render_API_GetAnnouncements(request):
	return API_GetAnnouncements(request)

def Render_API_DeleteAnnouncement(request):
	return API_DeleteAnnouncement(request)

def Render_API_API_MarkAsRead(request):
	return API_MarkAsRead(request)

@csrf_exempt
def Render_API_UploadFile(request):
	return API_UploadFile(request)

@csrf_exempt
def Render_API_PublishTreehole(request):
	return API_PublishTreehole(request)

def Render_API_GetTreehole(request):
	return API_GetTreehole(request)


#Added on 18/11
def Render_API_SetUserPriority(request):
	return API_SetUserPriority(request)

def Render_API_DeleteUser(request):
	return API_DeleteUser(request)

@csrf_exempt
def Render_API_CreateClass(request):
	return API_CreateClass(request)

def Render_API_GetClassInfoByIndex(request):
	return API_GetClassInfoByIndex(request)

def Render_API_GetAllClassInfo(request):
	return API_GetAllClassInfo(request)

def Render_API_DeleteClassByIndex(request):
	return API_DeleteClassByIndex(request)

#Comments Operations
@csrf_exempt
def Render_API_PublishComment(request):
	return API_PublishComment(request)

def Render_API_GetCommentsByID(request):
	return API_GetCommentsByID(request)

def Render_API_DeleteCommentByID(request):
	return API_DeleteCommentByID(request)

#Online Disk Operations
@csrf_exempt
def Render_API_AddFile(request):
	return API_AddFile(request)

def Render_API_ExploreFolder(request):
	return API_ExploreFolder(request)

def Render_API_CreateFolder(request):
	return API_CreateFolder(request)

def Render_API_DeleteFileOrFolder(request):
	return API_DeleteFileOrFolder(request)

#AJAX Authentication
def Render_API_CheckEmailAndUsername(request):
	return API_CheckEmailAndUsername(request)

#Schedule
@csrf_exempt
def Render_API_CreateEvent(request):
	return API_CreateEvent(request)

@csrf_exempt
def Render_API_GetEvent(request):
	return API_GetEvent(request)

@csrf_exempt
def Render_API_DeleteEvent(request):
	return API_DeleteEvent(request)

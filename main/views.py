from django.shortcuts import render
from django.shortcuts import render_to_response
from main.api_users import *
from django.views.decorators.csrf import csrf_exempt

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

def Render_APITest(request):
<<<<<<< HEAD
	return render_to_response("apitest.html",{})

def Render_Hello(request):
	return render_to_response("hello.html",{})
=======
	return render_to_response("apitest.html",{})
>>>>>>> 62eaae239e1b1b1771d0813d39f397efa0fdca60

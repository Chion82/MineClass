from django.shortcuts import render
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

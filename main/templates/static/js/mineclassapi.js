/************************************
**         Back-end JS API         **
**	Including Jquery is required   **	
*************************************/

API_ROOT = "";

/*api object: call all Back-end APIs*/
var api =
{
	/*APIs related to user operations*/
	"user" : 
	{
		/*
		function CreateUser(username,password,email,realname,classindex,sex,callback)
		Create a new user
		Input parameters: 	String username,	//username of the new user
							String password,	//password of the new user
							String email,		//email address of the new user
							String realname,	//real name of the new user
							int classindex,		//Index of the new user's class
							int sex,			//Index of the new user's sex
							function callback,	//Callback function called when this API call finishes. 
												//An object of results will be passed to this callback function
		Return value: none
		*/
		"CreateUser" :  function(username,password,email,realname,classindex,sex,callback)
						{
							$.post(API_ROOT + "api/createuser",
							{
								"username" : username,
								"password" : password,
								"email" : email,
								"realname" : realname,
								"classindex" : classindex,
								"sex" : sex,
							},
							function(data,status)
							{
								if(status=="success")
									callback(eval("("+data+")"));
								else
									callback({"error":1,"message":"Connection failed."});
							});
						},
		/*
		function Login(username,password)
		Login by passing username and password
		Input parameters: 	String username,	//username of the new user
							String password,	//password of the new user
							function callback,	//Callback function called when this API call finishes. 
												//An object of results will be passed to this callback function
		Return value: none
		*/
		"Login"    :  	function(username,password,callback)
						{
							$.post(API_ROOT + "api/login",
							{
								"username" : username,
								"password" : password,
							},
							function(data,status)
							{
								if(status=="success")
									callback(eval("("+data+")"));
								else
									callback({"error":1,"message":"Connection failed."});
							});
						},
		/*
		function UpdateSelfInfo(username,password,callback)
		Update user information using token stored in Cookie
		Input parameters: 	
							object
							{
								"email"		:  String email,		//email of the new user[optional]
								"realname"	:  String realname,	    //real name of the new user[optional]
								"birthday"  :  int birthday,		//unix timestamp of user's birthday[optional]
								"avatar"    :  String avatar,		//URL of avatar image[optional]
								"tag"       :  Array tag,			//Tags of the new user[optional]
								"classindex":  int classindex,		//Index of class[optional]
								"sex"       :  int sex				//Index of user's sex[optional]
							}
							function callback,	//Callback function called when this API call finishes. 
												//An object of results will be passed to this callback function
		Return value: none
		*/
		"UpdateSelfInfo":function(UserInfoObj,callback)
						{
							FieldToPost = UserInfoObj;
							$.post(API_ROOT + "api/updateselfinfo",
							FieldToPost,
							function(data,status)
							{
								if(status=="success")
									callback(eval("("+data+")"));
								else
									callback({"error":1,"message":"Connection failed."});
							});
						},
		/*
		function Logout()
		Logout using token stored in Cookie
		Input parameters: 	function callback,	//Callback function called when this API call finishes. 
												//An object of results will be passed to this callback function
		Return value: none
		*/
		"Logout"    :  	function(callback)
						{
							$.get(API_ROOT + "api/logout",
							function(data,status)
							{
								if(status=="success")
									callback(eval("("+data+")"));
								else
									callback({"error":1,"message":"Connection failed."});
							});
						},
		/*
		function GetUserInfo()
		Get user information using token stored in Cookie
		Input parameters: 	function callback,	//Callback function called when this API call finishes. 
												//An object of results will be passed to this callback function
		Return value: none
		*/
		"GetUserInfo" : function(callback)
						{
							$.get(API_ROOT + "api/getuserinfo",
							function(data,status)
							{
								if(status=="success")
									callback(eval("("+data+")"));
								else
									callback({"error":1,"message":"Connection failed."});
							});
						},
		/*
		function GetUserInfoByUsername()
		Get user information by passing usernames
		Input parameters: 	Array usernames,	//String Array
							function callback,	//Callback function called when this API call finishes. 
												//An object of results will be passed to this callback function
		Return value: none
		*/
		"GetUserInfoByUsername" : function(usernames,callback)
						{
							$.post(API_ROOT + "api/getuserinfobyusername",
							{
								"username" : usernames
							},
							function(data,status)
							{
								if(status=="success")
									callback(eval("("+data+")"));
								else
									callback({"error":1,"message":"Connection failed."});
							});
						},
		
	}
}; 
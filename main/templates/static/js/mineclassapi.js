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
			/*$.ajax({
				url: API_ROOT + "api/getuserinfo",
				type: 'GET',
				async: false,
				dataType: 'json',
				success:function(data,status)
						{
							if(status=="success")
								callback(eval("("+data+")"));
							else
								callback({"error":1,"message":"Connection failed."});
						},
			});*/							
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

		"SetUserPriority" : function(username,priority,callback)
		{
			$.get(API_ROOT + "api/setuserpriority?username="+encodeURIComponent(username)+"&priority="+encodeURIComponent(priority),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});
				});
		},
		
		"DeleteUser" : function(username,callback)
		{
			$.get(API_ROOT + "api/deleteuser?username="+encodeURIComponent(username),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});				
				});
		}
	},

	"class":
	{
		"CreateClass" : function(classindex,major,classname,period,callback)
		{
			$.post(API_ROOT+"api/createclass",
				{
					"classindex" : classindex,
					"major" : major,
					"classname" : classname,
					"period" : period,
				},
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});				
				}
				);
		},
		"GetClassInfoByIndex" : function(classindex,callback)
		{
			$.get(API_ROOT+"api/getclassinfobyindex?classindex="+encodeURIComponent(classindex),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});				
				});
		},
		"GetAllClassInfo" : function(callback)
		{
			$.get(API_ROOT + "api/getallclassinfo",
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});				
				});
		},
		"DeleteClassByIndex" : function(classindex,callback)
		{
			$.get(API_ROOT + "api/deleteclassbyindex",
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});				
				}
			);
		}
	},

	"announcement" :
	{
		"PublishAnnouncement" : function(announcement,tag /*Array of String*/,attachment/*Attachment Path*/,classindex/*Array of classindex*/,callback)
		{
			$.post(API_ROOT + "api/publishannouncement",
				{
					"announcement" : announcement,
					"tag" : tag,
					"attachment" : attachment,
					"class" : classindex
				},
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});				
				}
			);
		},
		"GetAnnouncements" : function(tag,page,callback)
		{
			URLTags="";
			for (var SingleTag in tag)
			{
				URLTags += ("&tag[]=" + encodeURIComponent(SingleTag));
			}
			$.get(API_ROOT + "api/getannouncements" + URLTags + "&page=" + page,
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		},
		
		"DeleteAnnouncement" : function(id,callback)
		{
			$.get(API_ROOT + "api/deleteannouncement?id=" + encodeURIComponent(id),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		},

		"MarkAsRead" : function(id,callback)
		{
			$.get(API_ROOT + "api/markasread?id=" + encodeURIComponent(id),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}				
			);
		}
	},

	"treehole" :
	{
		"PublishTreehole" : function(treehole,pic /*URL of image. use "" if no image*/,callback)
		{
			$.post(API_ROOT + "api/publishtreehole",
				{
					"treehole" : treehole,
					"pic" : pic
				},
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		},
	

		"GetTreehole" : function(page,callback)
		{
			$.get(API_ROOT + "api/gettreehole?page=" + page,
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}			
			);
		}
	},

	"comment" :
	{
		"PublishComment" : function(CommentType/* 0 for Announcements, 1 for Treeholes*/,comment,id,callback)	/*注意：此处id是公告或树洞的id*/
		{
			$.post(API_ROOT + "api/publishcomment",
				{
					"commenttype" : CommentType,
					"comment" : comment,
					"id" : id
				},
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		},

		"GetCommentsByID" : function(CommentType,id,callback)	/*注意：此处id是公告或树洞的id*/
		{
			$.get(API_ROOT + "api/getcommentsbyid?commenttype=" + CommentType + "id=" + encodeURIComponent(id),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		},

		"DeleteCommentByID" : function(id,callback)	/*此处id是评论的id*/
		{
			$.get(API_ROOT + "api/deletecommentbyid?id=" + encodeURIComponent(id),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		}
	},

	"disk" :
	{
		"AddFile" : function(FileName,folder,URL,callback)
		{
			$.post(API_ROOT + "api/addfile",
				{
					"filename" : FileName,
					"folder" : folder,
					"url" : URL
				},
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		},

		"ExploreFolder" : function(folder,callback)
		{
			$.get(API_ROOT + "api/explorefolder?folder=" + encodeURIComponent(folder),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		},

		"CreateFolder" : function(folder,callback)
		{
			$.get(API_ROOT + "api/createfolder?folder" + encodeURIComponent(folder),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		},

		"DeleteFileOrFolder" : function(IsFolder /* bool var*/,folder,filename/* use "" when deleting a folder*/, callback)
		{
			$.get(API_ROOT + "api/deletefileorfolder?isfolder=" + encodeURIComponent(IsFolder) + "&filename=" + encodeURIComponent(FileName) + "&folder=" + encodeURIComponent(folder),
				function(data,status)
				{
					if (status=="success")
						callback(eval("("+data+")"));
					else
						callback({"error":1,"message":"Connection failed."});					
				}
			);
		}
	}
}; 
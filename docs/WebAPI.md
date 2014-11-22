#users
##users.CreateUser
* URL
```
api/createuser
```
* 请求方式
```
POST
```
* 请求内容
```
username=testuser&password=123456&email=123@123.com&realname=张全蛋&sex=1&classindex=999 
//sex：0：男 1：女
//classindex：班级索引号
```
* 返回结果
```
{"code":0,"message":"Invalid paramaters."}		//参数有误
{"code":1,"message":"Username exists."}			//用户名已存在
{"code":2,"message":"Email exists."}			//Email已存在
{"code":3,"message":"User created."}			//成功创建用户
```
##users.Login
* URL
```
api/login
```
* 请求方式
```
POST
```
* 请求内容
```
username=test&password=test
```
* 返回结果
```
{"code":0,"message":"No such user."}
{"code":1,"message":"Password incorrect."}
{"code":2,"message":"Success.","token":"8b873174aa71a80b10229f39d277c4bb"}
```
##users.Logout
* URL
```
api/logout
```
* 请求方式
```
GET
```
* 请求内容
```
NULL
```
* 返回结果
```
{"code":0,"message":"Token invalid."}
{"code":1,"message":"Success."}
```
##users.UpdateSelfInfo
* URL
```
api/updateselfinfo
```
* 描述
```
更新当前登录用户的信息
```
* 请求方式
```
POST
```
* 请求内容
```
email=test@test.com&realname=王尼玛&birthday=1416651473&avatar=static/upload/1.jpg&sex=1&classindex=999&introduction=小孩子不要看暴漫&tag[]=逗比&tag[]=暴走&tag[]=testTag&password=test
//PS:参数可选，要更新什么就传什么参数
```
* 返回结果
```
{"code":0,"message":"Token invalid."}		//未登录
{"code":1,"message":"Update completed."}	//更新成功
```
##users.GetUserInfo
* URL
```
api/getuserinfo
```
* 描述
```
返回当前登录用户的信息
```
* 请求方式
```
GET
```
* 请求内容
```
NULL
```
* 返回结果
```
{"code":0,"message":"Token invalid."}
{"code":1,"message":"Success.","UserInfo":{'username': 'test', 'realname': '%E7%8E%8B%E5%B0%BC%E7%8E%9B', 'sex': 1, 'tag': ['%E9%80%97%E6%AF%94', '%E6%9A%B4%E8%B5%B0', 'testTag'], 'introduction': '%E5%B0%8F%E5%AD%A9%E5%AD%90%E4%B8%8D%E8%A6%81%E7%9C%8B%E6%9A%B4%E6%BC%AB', 'priority': 0, 'birthday': 1416651473, 'avatar': 'static/upload/1.jpg', 'classindex': 999, '_id': {'$oid': '544229df306b5b0f41495040'}, 'email': 'test@test.com', 'creatingtime': 1413622239}}
```
##users.GetUserInfoByUsername
* URL
```
api/getuserinfobyusername
```
* 描述
```
通过用户名获取用户信息，可同时获取多个用户信息
```
* 请求方式
```
POST
```
* 请求内容
```
username[]=test&username[]=testuser
```
* 返回结果
```
{"code":1,"message":"Success.","UserInfo":[{'username': 'test', 'realname': '%E7%8E%8B%E5%B0%BC%E7%8E%9B', 'sex': 1, 'tag': ['%E9%80%97%E6%AF%94', '%E6%9A%B4%E8%B5%B0', 'testTag'], 'introduction': '%E5%B0%8F%E5%AD%A9%E5%AD%90%E4%B8%8D%E8%A6%81%E7%9C%8B%E6%9A%B4%E6%BC%AB', 'priority': 0, 'birthday': 1416651473, 'avatar': 'static/upload/1.jpg', 'classindex': 999, '_id': {'$oid': '544229df306b5b0f41495040'}, 'email': 'test@test.com', 'creatingtime': 1413622239}, {'username': 'testuser', 'realname': '%E5%BC%A0%E5%85%A8%E8%9B%8B', 'sex': 1, 'tag': [], 'introduction': '', 'priority': 0, 'birthday': -1, 'avatar': 'static/upload/avatars/none.png', 'classindex': 999, '_id': {'$oid': '54704f08306b5b751bd677e1'}, 'email': '123@123.com', 'creatingtime': 1416646408}]}
```
##users.SetUserPriority
* URL
```
api/setuserpriority
```
* 描述
```
设置用户权限
PS：平民（priority=0）无此API调用权限，设置的其他用户的权限必须不大于当前用户的权限
PSS：关于权限:
	priority=0 		//平民
	priority=1 		//班委（可管理当前班级）
	priority=2 		//辅导员（可管理全部班级）
	priority=3		//管理员
```
* 请求方式
```
GET
```
* 请求内容
```
username=testuser&priority=1
```
* 返回结果
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Permission Denied."}
{"code":3,"message":"User doesn\'t exist."}
{"code":4,"message":"Success."}
```
##users.DeleteUser
* URL
```
api/deleteuser
```
* 描述
```
删除用户，只有管理员有该API的调用权限
```
* 请求方式
```
GET
```
* 请求内容
```
username=testuser
```
* 返回结果
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Permission Denied."}
{"code":3,"message":"User doesn\'t exist."}
{"code":4,"message":"Success."}
```
#class
##class.CreateClass
* URL
```
api/createclass
```
* 请求方式
```
POST
```
* 请求内容
```
classindex=123&major=挖掘机&classname=蓝翔三班&period=2014
```
* 返回结果
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Permission denied."}
{"code":2,"message":"Invalid Input."}
{"code":3,"message":"Class Index exists."}
{"code":4,"message":"Success."}
```
##class.GetClassInfoByIndex
* URL
```
api/getclassinfobyindex
```
* 请求方式
```
GET
```
* 请求内容
```
classindex=123
```
* 返回结果
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Class doesn\'t exist"}
{"code":3,"message":"Success.","ClassInfo": {"_id": {"$oid": "54707250306b5b751bd677e4"}, "classindex": 123, "classname": "%E8%93%9D%E7%BF%94%E4%B8%89%E7%8F%AD", "major": "%E6%8C%96%E6%8E%98%E6%9C%BA", "period": "2014"}}
```
##class.GetAllClassInfo
* URL
```
api/getallclassinfo
```
* 请求方式
```
GET
```
* 请求参数
```
NULL
```
* 返回结果
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Success.","ClassInfo": [{"classname": "%E8%93%9D%E7%BF%94%E4%B8%89%E7%8F%AD", "major": "%E6%8C%96%E6%8E%98%E6%9C%BA", "_id": {"$oid": "54707250306b5b751bd677e4"}, "period": "2014", "classindex": 123}]}
```
##class.DeleteClassByIndex
* URL
```
api/deleteclassbyindex
```
* 描述
```
只有管理员有该API的调用权限
```
* 请求方式
```
GET
```
* 请求参数
```
classindex=123
```
* 返回结果
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Permission denied."}
{"code":2,"message":"Invalid Input."}
{"code":3,"message":"Class doesn\'t exit"}
{"code":4,"message":"Success."}
```

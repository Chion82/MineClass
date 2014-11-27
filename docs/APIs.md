> #如何调用js.API？
* 1.在HTML中引入jquery库和mineclassapi.js
```html
<script type="text/javascript" src="static/js/jquery-1.11.1.min.js"></script>
<script type="text/javascript" src="static/js/mineclassapi.js"></script>
```
* 2.所有API函数均在api对象中分类定义好，直接在js中调用即可。eg：
```javascript
api.user.Login("test","test",function(result)
    			{
					alert(JSON.stringify(result));
				});
//用户登录
```
* 3.main/templates/apitest.html，API调用示例
* 4.关于Web API：正常情况下调用js.API即可。如果js.API因为各种原因暂时性失效，web API可用于临时测试

#api.user

##Login(username,password,callback)
* 说明：使用用户名和密码登录，若登录成功则返回AccessToken并设置token Cookie<br/>
* 传入参数：
```
String username, //用户名
String password //密码
function callback //回调函数，当收到服务器返回的JSON结果时自动调用该函数，并向该函数传入一个包含结果的对象（下同）
```
* 函数返回值：无。返回的结果会传入callback()中<br/>
* 回调函数传入对象：
```
object
{
	"code"    : int,	 	//0：用户不存在，1：密码错误，2：登录成功
	"message" : String,  	//错误信息
	"token"   : String    	//如果登陆成功，返回AccessToken
}
```
* 示例：
```javascript
api.user.Login("test"               //用户名
                ,"test",             //密码
                function(result)    //回调函数
    			{
					if(result.code==2)
                        alert("Success");
                    else
                        alert("Failed. message=" + result.message);
				});
```
##CreateUser(username,password,email,realname,classindex,sex,callback)
* 说明：创建一个用户
* 传入参数：
```
String username,                 //用户名
String password,                 //密码
String email,                    //Email
String realname,                 //真实姓名
int classindex,                  //班级的索引号
int sex,                         //性别，0：男，1：女
function callback                //回调函数
```
* 函数返回值：无。返回的结果会传入callback()中。
* 回调函数传入对象：
```
object
{
	"code"    : int, 	//0：参数错误，1：用户名已存在，2：邮箱已存在，3：成功
	"message" : String  //备注信息
}
```
* 示例：
```javascript
api.user.CreateUser("test","test","test@test.com","测试",999,0,
                    function(result){
                    	alert(JSON.stringify(result));
                    });
```
##UpdateSelfInfo(UserInfoObj,callback)
* 说明：更新用户自身信息，只能更新当前AccesToken对应的用户信息。PS：无需传入AccessToken，API会自动从Cookie中获取AccessToken。
* 传入参数：
```
Object UserInfoObject,			//包含需要更新信息的用户信息对象
function callback				//回调函数
```
* 用户信息对象：（对象内参数可选）
```
object
{
	"email"		:  String email,		//Email[optional]
	"realname"	:  String realname,	    //真实姓名[optional]
	"birthday"  :  int birthday,		//生日，UNIX时间戳（可以为负数）[optional]
	"avatar"    :  String avatar,		//头像文件路径[optional]
	"tag"       :  Array tag,			//标签数组，数组的每个元素是字符串[optional]
	"classindex":  int classindex,		//班级的索引号[optional]
	"sex"       :  int sex				//性别，男：0，女：1[optional]
}
```
* 函数返回值：无。返回的结果会传入callback()中。
* 回调函数传入对象：
```
object
{
	"code"    :  int,				//0：Cookie Token无效，1：成功
	"message" :  message			//备注
}
```
* 示例：
```javascript
api.user.UpdateSelfInfo(		//用户信息对象，只需添加需要更新的信息项
						{
							"birthday":0,						//生日，UNIX时间戳，支持负数
							tag:["测试","呵呵呵"],				//标签数组
							"email":"sdspeed82@hotmail.com"		//Email
						},
						function(result){
							alert(JSON.stringify(result));
						}
						);
```
##GetUserInfo(callback)
* 获取当前用户的信息
* 调用示例
```
api.user.GetUserInfo(function(result){
	alert(result.email);
});
```
* 返回结果
```
{"code":0,"message":"Token invalid."}
{"code":1,"message":"Success.","UserInfo":{'username': 'test', 'realname': '%E7%8E%8B%E5%B0%BC%E7%8E%9B', 'sex': 1, 'tag': ['%E9%80%97%E6%AF%94', '%E6%9A%B4%E8%B5%B0', 'testTag'], 'introduction': '%E5%B0%8F%E5%AD%A9%E5%AD%90%E4%B8%8D%E8%A6%81%E7%9C%8B%E6%9A%B4%E6%BC%AB', 'priority': 0, 'birthday': 1416651473, 'avatar': 'static/upload/1.jpg', 'classindex': 999, '_id': {'$oid': '544229df306b5b0f41495040'}, 'email': 'test@test.com', 'creatingtime': 1413622239}}
```
##GetUserInfoByName(usernames,callback)
* 调用示例
```
api.user.GetUserInfoByUsername(["admin","test"],function(result){
	alert(result.UserInfo.realname);
});
```
* 返回结果
```
{"code":1,"message":"Success.","UserInfo":[{'username': 'test', 'realname': '%E7%8E%8B%E5%B0%BC%E7%8E%9B', 'sex': 1, 'tag': ['%E9%80%97%E6%AF%94', '%E6%9A%B4%E8%B5%B0', 'testTag'], 'introduction': '%E5%B0%8F%E5%AD%A9%E5%AD%90%E4%B8%8D%E8%A6%81%E7%9C%8B%E6%9A%B4%E6%BC%AB', 'priority': 0, 'birthday': 1416651473, 'avatar': 'static/upload/1.jpg', 'classindex': 999, '_id': {'$oid': '544229df306b5b0f41495040'}, 'email': 'test@test.com', 'creatingtime': 1413622239}, {'username': 'testuser', 'realname': '%E5%BC%A0%E5%85%A8%E8%9B%8B', 'sex': 1, 'tag': [], 'introduction': '', 'priority': 0, 'birthday': -1, 'avatar': 'static/upload/avatars/none.png', 'classindex': 999, '_id': {'$oid': '54704f08306b5b751bd677e1'}, 'email': '123@123.com', 'creatingtime': 1416646408}]}
```
##LogOut(callback)
```
api.user.Logout(function(result){
	alert(JSON.stringify(result));
});
```
```
{"code":0,"message":"Token invalid."}
{"code":1,"message":"Success."}
```
##CheckEmailAndUsername(email,username,callback)
```
api.user.CheckEmailAndUsername(
	"123@qq.com",
	"test",
	function(result)
	{
		alert(result.message);
	}
);
```
```
{"code":0,"message":"Username exists."}
{"code":1,"message":"Email exists."}
{"code":2,"message":"OK."}
```
##SetUserPriority(username,priority,callback)
* 说明
> 设置用户权限
PS：平民（priority=0）无此API调用权限，设置的其他用户的权限必须不大于当前用户的权限
PSS：关于权限:
	priority=0 		//平民
	priority=1 		//班委（可管理当前班级）
	priority=2 		//辅导员（可管理全部班级）
	priority=3		//管理员

```
api.user.SetUserPriority("test",3,
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Permission Denied."}
{"code":3,"message":"User doesn't exist."}
{"code":4,"message":"Success."}
```
##DeleteUser(username,callback)
> 只有管理员（priority=3）有此权限

```
api.user.DeleteUser("helloworld",
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Permission Denied."}
{"code":3,"message":"User doesn\'t exist."}
{"code":4,"message":"Success."}
```

#api.class
##CreateClass(classindex,major,classname,period,callback)
```
api.class.CreateClass(555,"挖掘机2号","新东方2班","2014",
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Permission denied."}
{"code":2,"message":"Invalid Input."}
{"code":3,"message":"Class Index exists."}
{"code":4,"message":"Success."}
```
##GetClassInfoByIndex(classindex,callback)
```
api.class.GetClassInfoByIndex(555,
	function(result)
	{
		alert(result.ClassInfo.classname);
	}
);
```
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Class doesn\'t exist"}
{"code":3,"message":"Success.","ClassInfo": {"_id": {"$oid": "54707250306b5b751bd677e4"}, "classindex": 123, "classname": "%E8%93%9D%E7%BF%94%E4%B8%89%E7%8F%AD", "major": "%E6%8C%96%E6%8E%98%E6%9C%BA", "period": "2014"}}
```

##GetAllClassInfo(callback)
```
api.class.GetAllClassInfo(
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Success.","ClassInfo": [{"classname": "%E8%93%9D%E7%BF%94%E4%B8%89%E7%8F%AD", "major": "%E6%8C%96%E6%8E%98%E6%9C%BA", "_id": {"$oid": "54707250306b5b751bd677e4"}, "period": "2014", "classindex": 123}]}
```
##DeleteClassByIndex(classindex,callback)
> 只有管理员有此权限

```
api.class.DeleteClassByIndex(555,
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Invalid Token."}
{"code":1,"message":"Permission denied."}
{"code":2,"message":"Invalid Input."}
{"code":3,"message":"Class doesn\'t exit"}
{"code":4,"message":"Success."}
```
#api.announcement
##PublishAnnouncement(announcement,tag /\*Array of String\*/,attachment/\*Attachment Path\*/,classindex/\*Array of classindex\*/,callback)
```
api.announcement.PublishAnnouncement(
	"这是一条测试公告",
	['test1','test2','haha'],
	'',	//没有附件
	[555,123,999],	//可见该公告的班级，对于权限为0或1的用户此参数无效，其发布的公告只有其所在班级可见
	function(result)
	{
		alert(JSON.stringify(result));
	}
	);
```
```
{"code":0,"message":"AccessToken invalid. Please login first."}
{"code":1,"message":"Empty content."}
{"code":2,"message":"Success."}
```
##GetAnnouncements(tag,page,callback)
```
api.announcement.GetAnnouncements(
	[],//传入tag数组可以按tag筛选公告
	1,//page
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
/* FAILED */
{"code":0,"message":"AccessToken invalid. Please login first."}

/* SUCCEEDED */
[{"classes":[999],"announcement":"HelloWorld","tag":["TAG1","TAG2","TAG3"],"PublishmentTime":1414826581,"publisher":"test","publisher_realname":"%E7%8E%8B%E5%B0%BC%E7%8E%9B","_id":{"$oid":"54548a55306b5b56636a6733"},"publisher_avatar":"static/upload/1416842959663394.jpg","ReadUsers":[],"attachment":"none"},{"classes":[999],"announcement":"testing","tag":[],"PublishmentTime":1414825324,"publisher":"test","publisher_realname":"%E7%8E%8B%E5%B0%BC%E7%8E%9B","_id":{"$oid":"5454856c306b5b5497754a0f"},"publisher_avatar":"static/upload/1416842959663394.jpg","ReadUsers":[],"attachment":"none"}]
```
##DeleteAnnouncement(id,callback)
```
api.announcement.DeleteAnnouncement(
	"123456789012345678901234",	//必须为24位字符串
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Please login first."}
{"code":1,"message":"Invalid input"}
{"code":2,"message":"Invalid id"}
{"code":3,"message":"Permission denied."}
{"code":4,"message":"Success in deleting announcement."}
```
##MarkAsRead(id,callback)
> 标记公告为已阅

```
api.announcement.MarkAsRead(
	"123456789012345678901234",
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Please login first."}
{"code":1,"message":"Invalid input"}
{"code":2,"message":"Invalid id"}
{"code":3,"message":"Success."}
```

#api.treehole
##PublishTreehole(treehole,pic /\*URL of image. use "" if no image\*/,callback)
```
api.treehole.PublishTreehole(
	"老子今天萌萌哒！！",
	"",
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Empty treehole content."}
{"code":1,"message":"Success."}
```
##GetTreehole(page,callback)
```
api.treehole.GetTreehole(
	1,
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
[{"_id": {"$oid": "547209a2306b5b3372863f5a"}, "pic": "none", "PublishmentTime": 1416759712, "treehole": "%E8%80%81%E5%AD%90%E4%BB%8A%E5%A4%A9%E8%90%8C%E8%90%8C%E5%93%92%EF%BC%81%EF%BC%81"}, {"_id": {"$oid": "54551bd0306b5b141fe40df5"}, "pic": "none", "PublishmentTime": 1414863822, "treehole": "NoPics"}, {"_id": {"$oid": "54551b65306b5b141fe40df4"}, "pic": "static/upload/1414863210930578.jpg", "PublishmentTime": 1414863715, "treehole": "%E6%B5%8B%E8%AF%95%EF%BC%8C%E6%96%9C%E7%9C%BC%E7%AC%91"}]
```

#api.comment
##PublishComment(CommentType/\* 0 for Announcements, 1 for Treeholes\*/,comment,id,callback)
> 向指定ID（_id.$oid）的公告或树洞发表评论

```
api.comment.PublishComment(
	0,	//0为公告评论，1为树洞评论
	"测试评论 哈哈哈 testing",
	"54717110306b5b3265a79746",	//公告或树洞的ID，通过_id.$oid获得
	function(result)
	{
		alert(JSON.stringify(result));
	}					
);
```
```
{"code":0,"message":"Invalid AccessToken."}
{"code":1,"message":"Invalid Input"}
{"code":2,"message":"Invalid ID."}
{"code":3,"message":"Success."}
```
##GetCommentsByID(CommentType,id,callback)
> 通过公告或树洞的ID（通过_id.$oid获得）获取评论

```
api.comment.GetCommentsByID(
	0,
	"54717110306b5b3265a79746",
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Invalid AccessToken."}
{"code":1,"message":"Invalid Input."}
{"code":3,"message":"Success.","comments":[{"comment":"%E6%B5%8B%E8%AF%95%E8%AF%84%E8%AE%BA%26amp%3Bnbsp%3B%E5%93%88%E5%93%88%E5%93%88%26amp%3Bnbsp%3Btesting","publisher":"test","PublishmentTime":1416759352,"publisher_avatar":"static/upload/1416842959663394.jpg","CommentType":0,"objid":"54717110306b5b3265a79746","publisher_realname":"%E7%8E%8B%E5%B0%BC%E7%8E%9B","_id":{"$oid":"54720838306b5b3372863f57"}},{"comment":"%E6%B5%8B%E8%AF%95%E8%AF%84%E8%AE%BA%26amp%3Bnbsp%3B%E5%93%88%E5%93%88%E5%93%88%26amp%3Bnbsp%3Btesting","publisher":"test","PublishmentTime":1416759933,"publisher_avatar":"static/upload/1416842959663394.jpg","CommentType":0,"objid":"54717110306b5b3265a79746","publisher_realname":"%E7%8E%8B%E5%B0%BC%E7%8E%9B","_id":{"$oid":"54720a7d306b5b3372863f5c"}}]}
```
##DeleteCommentByID(id,callback)
> 通过评论ID（_id.$oid）删除评论。注意：此处ID为评论的ID，而非公告或树洞的ID

```
api.comment.DeleteCommentByID(
	"123456789012345678901234",
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"Invalid AccessToken."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Permission Denied."}
{"code":3,"message":"Invalid ID"}
{"code":4,"message":"Success."}
```

#api.disk
> 云硬盘（资源共享）模块

##AddFile(FileName,folder,URL,callback)
> 添加文件

```
api.disk.AddFile(
	"testFile.jpg",		//虚拟文件名，用于识别文件，不一定要跟URL真实文件名相同
	"home/subfolder",	//用于存放该文件的虚拟目录，注意：目录头尾均不带斜杠
	"static/upload/avatars/1.jpg",	//真实URL，通过POST文件到api/upload后获得
	function(result)
	{
		alert(JSON.stringify(result));
	}					
);
```
```
{"code":0,"message":"AccessToken invalid. Please login first."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Folder doesn't exist"}
{"code":3,"message":"File exists."}
{"code":4,"message":"Success."}
```
##ExploreFolder(folder,callback)
> 浏览虚拟目录

```
api.disk.ExploreFolder(
	"home/subfolder",
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"AccessToken invalid. Please login first."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Folder doesn't exist"}
{"code":3,"message":"Success","files":[{"URL": "static/upload/avatars/1.jpg", "folder": "home/subfolder", "_id": {"$oid": "54720912306b5b3372863f58"}, "uploader": "test", "FileName": "testFile.jpg"}],"folders":[]}
```
##CreateFolder(folder,callback)
```
api.disk.CreateFolder(
	"home/newfolder",
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"AccessToken invalid. Please login first."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Folder exists"}
{"code":3,"message":"Success."}
```
##DeleteFileOrFolder(IsFolder /\* bool var\*/,folder,FileName/\* use "" when deleting a folder\*/, callback)
> 删除虚拟文件或虚拟目录，删除目录时IsFolder参数传1，FileName参数传空字符串

```
api.disk.DeleteFileOrFolder(
	0,	/*Is Folder?*/
	"home/subfolder",
	"testFile.jpg",
	function(result)
	{
		alert(JSON.stringify(result));
	}
);
```
```
{"code":0,"message":"AccessToken invalid. Please login first."}
{"code":1,"message":"Invalid Input."}
{"code":2,"message":"Folder or file doesn't exist"}
{"code":3,"message":"Permission Denied."}
{"code":4,"message":"Success."}
```

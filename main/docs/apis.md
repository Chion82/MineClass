#如何调用js.API？
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
用户信息处理

##1.Login(username,password,callback)
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
##2.CreateUser(username,password,email,realname,classindex,sex,callback)
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
##3.UpdateSelfInfo(UserInfoObj,callback)
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
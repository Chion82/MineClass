/*
*user常用函数
*需同时引入mineclassapi.js跟jquery才能使用
*而且一定要比该js先引入
*/

/*实现点击头像弹出菜单*/
function showOverflow(){
  var oBtn=document.getElementById('head-avatar');
  var oDiv=document.getElementById('action-overflow');
 oBtn.onclick=function(ev){
  var oEvent=ev||event;
  $("#action-overflow").slideToggle('slow/200/fast', function() {});
   oEvent.cancelBubble=true;
  }              //取消冒泡
 document.onclick=function(){
  $("#action-overflow").slideUp('slow/200/fast', function() {});
  } 
}

/*点击add出现输入框*/
//TODO
//弃用

//退出
function Logout(){
    api.user.Logout(function(result){
      var myresult = eval(result);
      if(myresult.code=="1")window.location.href="home_page";
      else alert("退出似乎出了点问题，你可以反馈给我们。");
    });
}
//test
function showDiscuss(){
  $("#showDiscuss").click(function(event) {
    if($("#discussArea").is(':hidden')){
      $("#discussArea").slideDown('slow/400/fast', function() {});
    }else{
      $("#discussArea").slideUp('slow/400/fast', function() {});
    }
  }); 
}
//注册
function  registValid() {
    $("#regist").validate(
              {
                  /*自定义验证规则*/
                  rules: {
                    email:{
                        email:true,
                        required:true
                      },
                    pass: {
                         required: true,
                         maxlength:16,
                         minlength: 6
                      },
                    confirmpass: {
                         required: true,
                         //maxlength:16,
                         //minlength: 6,
                         equalTo: "#pass"
                      }
                  },      
                  /*错误提示位置*/
                  errorPlacement: function (error, element) {
                    if(element.is("#email")){
                      error.appendTo(".email-error");
                    }else if(element.is("#pass")){
                      error.appendTo('.pass-error');
                    }else if(element.is("#confirmpass")){
                      error.appendTo('.confirmpass-error');
                    }
                  },
                  /*提示信息*/
                  messages: {
                    email: {
                        required: "请输入Email地址",
                        email: "请输入正确的email地址"
                       },
                       pass: {
                        required: "请输入密码",
                        minlength: "密码长度为6-16个字符",
                        maxlength: "密码长度为6-16个字符"
                       },
                       confirmpass: {
                        required: "请确认密码",
                        //minlength: "确认密码不能小于6个字符",
                        equalTo: "两次输入密码不一致"
                       }
                  },
                  /*提交信息*/
                  submitHandler:function(form){
                  $("#registSubmit").attr("value","注册中……");
                  $()
                  { 
                      var names=["m","i","n","e","c","l","a","s"];
                      var classindex=1*($("#level option:selected").val()+$("#academy option:selected").val()+$("#major option:selected").val()+$("#class option:selected").val());
                      //alert("123");
                      api.user.CreateUser(
                        $("#email").val(),//用户名
                        $("#pass").val(),
                        $("#email").val(),//邮箱
                        "小"+names[Math.floor(Math.random()*8)],//昵称，随机mineclass中的一个
                        classindex,//班级序号，这里暂时处理为4个String值相加
                        1,//默认女生
                        function(result){
                        var myresult = eval(result);
                        if(myresult.code==3){
                      //手动登录
                      api.user.Login(
                        $("#email").val(),
                        $("#pass").val(),
                          function(result){
                          });
                        //跳转到公告                                          
                          window.location.href="inform";
                        }
                        else if(myresult.code==0)alert("参数错误");
                        else if(myresult.code==1||myresult.code==2){
                          $("#infoSubmit").attr("value","保存中……");
                          $(".email-error").text('邮箱已被注册，请直接登录');
                        }
                        }
                      );
                    }
                  },
                  //更多
              }
    );
}
//登录
function  loginValid() {
    $("#login").validate(
              {
                  /*自定义验证规则*/
                  rules: {
                    email:{
                        email:true,
                        required:true
                      },
                    pass: {
                         required: true,
                         minlength: 6,
                         maxlength:16
                      }
                  },      
                  /*错误提示位置*/
                  errorPlacement: function (error, element) {
                    if(element.is("#email")){
                      error.appendTo(".email-error");
                    }else if(element.is("#pass")){
                      error.appendTo('.pass-error');
                    }
                  },
                  /*提示信息*/
                  messages: {
                    email: {
                        required: "请输入Email地址",
                        email: "请输入正确的email地址"
                       },
                       pass: {
                        required: "请输入密码",
                        minlength: "密码长度为6-16个字符",
                        maxlength:"密码长度为6-16个字符"
                       }
                  },
                  /*提交信息*/
                  submitHandler:function(form){
                  $("#loginSubmit").attr("value","登录中……");
                  $()
                  { 
                      //登录
                      api.user.Login(
                        $("#email").val(),
                        $("#pass").val(),
                      function(result){
                            var myresult = eval(result);
                        if(myresult.code==2)window.location.href="inform";     
                        else if(myresult.code==0){
                          $("#infoSubmit").attr("value","保存");
                          $(".email-error").text('用户不存在，请先注册');
                        }
                        else if(myresult.code==1||myresult.code==2){
                          $("#infoSubmit").attr("value","保存");
                          $(".pass-error").text('密码错误，请重新输入');
                        }
                      }
                      );
                    }
                  },
                  //更多
              }
    );
}
//修改密码
function modifyPassword(){
    $("#modifyPassword").validate(
              {
                  /*自定义验证规则*/
                  rules: {
                    oldpass:{
                        minlength: 6,
                        maxlength:16,
                        required:true
                      },
                    newpass: {
                         required: true,
                         maxlength:16,
                         minlength: 6
                      },
                    confirmpass:{
                          required:true,
                          equalTo:"#newpassword"
                    }
                  },      
                  /*错误提示位置*/
                  errorPlacement: function (error, element) {
                    if(element.is("#oldpassword")){
                      error.appendTo(".oldpassword-error");
                    }else if(element.is("#newpassword")){
                      error.appendTo('.newpassword-error');
                    }else if(element.is("#confirmpassword")){
                      error.appendTo('.confirmpassword-error');
                    }
                  },
                  /*提示信息*/
                  messages: {
                    oldpass: {
                        required: "请输入当前密码",
                        minlength: "密码长度为6-16个字符",
                        maxlength:"密码长度为6-16个字符"
                       },
                    newpass: {
                        required: "请输入新密码",
                        minlength: "密码长度为6-16个字符",
                        maxlength:"密码长度为6-16个字符"
                       },
                    confirmpass:{
                        required:"请确认密码",
                        equalTo:"两次输入密码不一致"
                    }
                  },
                  /*提交信息*/
                  submitHandler:function(form){
                  $("#passSubmit").attr("value","保存中……");
                  $()
                  { 
                      //修改密码API

                    }
                  },
                  //更多
              }
    );  
}
//修改信息
function modifyInfo(){
    $("#modifyInfo").validate(
              {
                  /*自定义验证规则*/
                  rules: {//name，不是id
                    nickname:{
                        maxlength:20,
                        required:true
                      }
                  },      
                  /*错误提示位置*/
                  errorPlacement: function (error, element) {
                    if(element.is("#nick")){
                      error.appendTo(".nick-error");
                    }
                  },
                  /*提示信息*/
                  messages: {
                    nickname: {
                        required: "请输入昵称",
                       }
                  },
                  /*提交信息*/
                  submitHandler:function(form){
                  $("#infoSubmit").attr("value","保存中……");
                  $()
                  { 
                    var classindex=1*($("#level option:selected").val()+$("#academy option:selected").val()+$("#major option:selected").val()+$("#class option:selected").val());
                      //API
                    api.user.UpdateSelfInfo({
                      "realname":$("#nick").val(),//昵称
                      tag:[$("#job option:selected").val()],//我是
                      "classindex":classindex,//班级
                      "sex":1*($("input[name='sex']:checked").val()),//性别
                    },
                      function(result){
                        var myresult = eval(result);
                        if(myresult.code==1){
                          $("#infoSubmit").attr("value","保存");
                          //success一些提示
                        }else{
                          //failed
                        }
                      });
                    }
                  },
                  //更多
              }
    );  
}
//setInfo初始化信息
function initInfo(){
  api.user.GetUserInfo(function(result){
    var infoResult = eval(result);
      //设置昵称
      $("#nick").attr("value",infoResult.UserInfo.realname);
      //我是
      if(infoResult.UserInfo.tag=='0'){
        $("#job option[value='0']").attr('selected', true);//平民
      }else if(infoResult.UserInfo.tag=='1'){
        $("#job option[value='1']").attr('selected', true);//班长
      }else if(infoResult.UserInfo.tag=='2'){
        $("#job option[value='2']").attr('selected', true);//团支书
      }else if(infoResult.UserInfo.tag='3'){
        $("#job option[value='3']").attr('selected', true);//学习委员
      }else{
        alert("职位job错误");
      }
      //班级部分
      if(infoResult.UserInfo.classindex==0){
        $("#level option[value='0']").attr('selected', true);
      }else if(infoResult.UserInfo.classindex==1000){
        $("#level option[value='1']").attr('selected', true);
      }else if(infoResult.UserInfo.classindex==2000){
        $("#level option[value='1']").attr('selected', true);
      }else if(infoResult.UserInfo.classindex==3000){
        $("#level option[value='1']").attr('selected', true);
      }else{
        alert("班级classindex错误");
      }
      //性别
      if(infoResult.UserInfo.sex==1){
        $("input[name='sex'][value='1']").attr("checked",true);//女生
      }else if(infoResult.UserInfo.sex==0){
        $("input[name='sex'][value='0']").attr("checked",true);//男生
      }else{
        alert("性别sex错误");
      }      
  });
}
//判断当前是否已经登录，未登录将跳转到首页
function isLogin(){
    api.user.GetUserInfo(function(result){
      var infoResult = eval(result);
      if(infoResult.code==0){
        window.location.href="home_page";
      }
    });
}
//显示头像
function showAvatar(){
    api.user.GetUserInfo(function(result){
      var infoResult = eval(result);
      $("#head-avatar").attr('src', infoResult.UserInfo.avatar);
    });
}
//显示选择头像的预览图
function showAvatarPreview(){
    api.user.GetUserInfo(function(result){
      var infoResult = eval(result);
      $("#head-preview").attr('src', infoResult.UserInfo.avatar);
    });
}
//显示编辑器
function showInput(){
    api.user.GetUserInfo(function(result){
      var infoResult = eval(result);
      if(infoResult.UserInfo.tag!='0'){
        $("#addarea").slideDown('slow/400/fast', function() {});
      }
    });
}

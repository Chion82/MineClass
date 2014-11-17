/*
*user常用函数
*需同时引入mineclassapi.js跟jquery才能使用
*而且一定要比该js先引入
*/

/*实现点击头像弹出菜单*/
function showOverflow()
  {
   var oBtn=document.getElementById('head-avatar');
    var oDiv=document.getElementById('action-overflow');
 oBtn.onclick=function(ev)
 { var oEvent=ev||event;
   if(oDiv.style.display=='block'){
        oDiv.style.display='none';
   }else{ 
   oDiv.style.display='block';
   oEvent.cancelBubble=true;
    }
}              //取消冒泡
 document.onclick=function()
 {oDiv.style.display='none';} 
 }

/*点击add出现输入框*/
//TODO

//退出
function Logout(){
    api.user.Logout(function(result){
      var myresult = eval(result);
      if(myresult.code=="1")window.location.href="home_page";
      else alert("退出似乎出了点问题，你可以反馈给我们。");
    });
}

function showDiscuss(){
  var disButton=document.getElementById('showDiscuss');
  var disArea=document.getElementById('discussArea');
  disButton.onclick=function(){
    if(disArea.style.display=='block'){
        disArea.style.display='none';
   }else{ 
   disArea.style.display='block';
    }
  }  
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
                         minlength: 6
                      },
                    confirmpass: {
                         required: true,
                         minlength: 6,
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
                        minlength: "密码长度不能小于{0}个字符"
                       },
                       confirmpass: {
                        required: "请输入确认密码",
                        //minlength: "确认密码不能小于6个字符",
                        equalTo: "两次输入密码不一致"
                       }
                  },
                  /*提交信息*/
                  submitHandler:function(form){
                  $("#registSubmit").attr("value","创建账户……");
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
                        0,//默认女生
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
                        else if(myresult.code==1||myresult.code==2)$(".email-error").text('邮箱已被注册，请直接登录');
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
                         minlength: 6
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
                        minlength: "密码长度不能小于{0}个字符"
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
                        else if(myresult.code==0)$(".email-error").text('用户不存在，请先注册');
                        else if(myresult.code==1||myresult.code==2)$(".pass-error").text('密码错误，请重新输入');
                        }
                      );
                    }
                  },
                  //更多
              }
    );
}
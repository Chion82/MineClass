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
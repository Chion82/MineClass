/**公告所需函数
*需引入jquery和umeditor
*/

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
//提交信息和清除信息
function publishInform(um){
	$("#clearAll").click(function(event) {
        um.execCommand('cleardoc');//清空输入框
	});
	$("#commit").click(function(event) {
		if(!um.hasContents()){
			um.setContent("不说点什么吗？");
		}else{
			var content=um.getContent();
			api.announcement.PublishAnnouncement(
					content,
					[],
					'',	//没有附件
					[],	//可见该公告的班级，对于权限为0或1的用户此参数无效，其发布的公告只有其所在班级可见
					function(result)
					{
						alert(JSON.stringify(result));
						//TODO 处理发布公告后的事件
					}
					);
		}
	});
}
//生成一页的内容
function createPage(num){
	var page;
	var item;	
	$(".mylist-wrap").append("<img id='loading' src='static/images/loading.gif'>");
	api.announcement.GetAnnouncements(
					[],//传入tag数组可以按tag筛选公告
					num,//page
					function(result)
					{
						for(var i=0;i<result.length;i++){
						var unixtime = new Date(result[i].PublishmentTime*1000);
						unixtime = unixtime.toLocaleString();	
						item="<div class='mylist'><div class='head'></div><div class='content'><div class='maincontentBG'><div class='maincontent'><div class='who'><div><img  class='head' src='static/images/ic_head.png' alt=''></div><div id='name'>"+decodeURIComponent(result[i].publisher)+"</div></div><div class='text'>"+decodeURIComponent(result[i].announcement)+"</div><div class='actionbar'><div class='time'>"+unixtime+"</div><div class='optiontab'><span class='option'><a href='javascript:void(0)'>10已阅</a></span><span class='option'><a href='javascript:void(0)' id='showDiscuss'>评论</a></span></div></div></div></div></div></div>";
						page+=item;
						}
						$("#loading").remove();
						$(".mylist-wrap").append(page);
						num++;
						scollToLoading(num);
					}
				);
}
//下拉到底部加载
function scollToLoading(num){
		var range = 50;             //距下边界长度/单位px
        var elemt = 500;           //插入元素高度/单位px
        var maxnum = 20;            //设置加载最多次数
        var totalheight = 0; 
        var main = $(".mylist");                     //主体元素
        $(window).scroll(function(){
            var srollPos = $(window).scrollTop();    //滚动条距顶部距离(页面超出窗口的高度)
            
            //console.log("滚动条到顶部的垂直高度: "+$(document).scrollTop());
            //console.log("页面的文档高度 ："+$(document).height());
            //console.log('浏览器的高度：'+$(window).height());
			
            totalheight = parseFloat($(window).height()) + parseFloat(srollPos);
    		if(($(document).height()-range) <= totalheight  && num != maxnum) {
                createPage(num);
            }
        });	
}
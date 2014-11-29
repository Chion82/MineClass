/**公告所需函数
*需引入jquery和umeditor
*/

//test
function showDiscuss1(){
  $(".showDiscuss1").click(function(event) {
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
	var page="";
	var item="";
	isLoading=true;
	console.log("createPage开始时的isLoading--"+isLoading);	
	//$(".mylist-wrap").append("<img id='loading' src='static/images/loading.gif'>");
	api.announcement.GetAnnouncements(
					[],//传入tag数组可以按tag筛选公告
					num,//page
					function(result)
					{
						console.log("result--"+result);
						if(result==""){
							isEnd=true;
							$(".mylist-wrap").append("<h1>已到达底部</h1>");
						}else{
							for(var i=0;i<result.length;i++){
							var unixtime = new Date(result[i].PublishmentTime*1000);
							unixtime = unixtime.toLocaleString();	
							item="<div class='mylist'><div class='head'></div><div class='content'><div class='maincontentBG'><div class='maincontent'><div class='who'><div><img  class='head' src='"+result[i].publisher_avatar+"' alt=''></div><div id='name'>"+decodeURIComponent(result[i].publisher_realname)+"</div></div><div class='text'>"+decodeURIComponent(result[i].announcement)+"</div><div class='actionbar'><div class='time'>"+unixtime+"</div><div class='optiontab'><span class='option'><a href='javascript:void(0)'>10已阅</a></span><span class='option'><a href='javascript:void(0)' class='showDiscuss' id='"+result[i]._id.$oid+"'>评论</a></span></div></div></div></div>    <div class='discussBG' area-id='"+result[i]._id.$oid+"'><div class='discuss'><div class='adddiscuss'><input type='text' class='discussInput'><button class='commitDiscuss' btn-id='"+result[i]._id.$oid+"'><span>发 表</span></button></div><div class='alldiscuss'>  <ul class='fillComment' content-id='"+result[i]._id.$oid+"'></ul>  </div></div></div></div></div>";
							page+=item;
							}
						//$('#loading').remove();
						$('.mylist-wrap').append(page);
						isLoading=false;
						}
					}
				);
}
/*下拉到底部加载
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
}*/
//显示评论区
function showDiscuss(type){
	var commentItem;
	var commentAll;
	$(".showDiscuss").click(function(event) {
		console.log("评论被点击");
		var btnID=$(this).attr("id");
		console.log("ID是"+btnID);
		$('div[area-id='+btnID+']').slideToggle("slow/400/fast");
		api.comment.GetCommentsByID(
    		type,
    		btnID,
    		function(result)
    		{
        		while(result[i]!=""){
        			commentItem="<li class='item'><div class='head'><img src='"+result[i].publisher_avatar+"' alt=''></div><div class='discusscontent'><span class='who'>"+decodeURIComponent(result[i].publisher_realname)+"</span><span class='maincontent_ds'>"+decodeURIComponent(result[i].comment)+"</span></div></li>"
        			commentAll+=commentItem;
        		}
        		$('.fillComment').append(commentAll);
    		}
		);

	});
}
//发布评论
function publishComment(type){
	$('.commitDiscuss').click(function(event) {
		console.log($(this).find('input').val());
		console.log($(this).find('ul').attr("content-id"));
		api.comment.PublishComment(
    		type,  //0为公告评论，1为树洞评论
    		$(this).find('input').val(),
    		$(this).find('ul').attr("content-id"), //公告或树洞的ID，通过_id.$oid获得
    		function(result)
    		{
    			//TODO
        		$(this).find('ul').append($(this).find('input').val());
    		}                   
		);

	});
}

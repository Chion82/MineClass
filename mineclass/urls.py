from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mineclass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #API: users
    url(r'^api/createuser$','main.views.Render_API_CreateUser'),
    url(r'^api/updateselfinfo$','main.views.Render_API_UpdateSelfInfo'),
    url(r'^api/login$','main.views.Render_API_Login'),
    url(r'^api/logout$','main.views.Render_API_Logout'),
    url(r'^api/getuserinfo$','main.views.Render_API_GetUserInfo'),
    url(r'^api/getuserinfobyusername$','main.views.Render_API_GetUserInfoByUsername'),

    #API: announcements

    url(r'^api/publishannouncement$','main.views.Render_API_PublishAnnouncement'),
    url(r'^api/getannouncements$','main.views.Render_API_GetAnnouncements'),
    url(r'^api/deleteannouncement$','main.views.Render_API_DeleteAnnouncement'),

    #API: UploadFile

    url(r'^api/upload$','main.views.Render_API_UploadFile'),

    #API: Treehole

    url(r'^api/publishtreehole$','main.views.')

    #Testing page
    url(r'^apitest$','main.views.Render_APITest'),
)

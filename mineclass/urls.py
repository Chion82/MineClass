<<<<<<< HEAD
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mineclass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #API: user
    url(r'^api/createuser$','main.views.Render_API_CreateUser'),
    url(r'^api/updateselfinfo$','main.views.Render_API_UpdateSelfInfo'),
    url(r'^api/login$','main.views.Render_API_Login'),
    url(r'^api/logout$','main.views.Render_API_Logout'),
    url(r'^api/getuserinfo$','main.views.Render_API_GetUserInfo'),
    url(r'^api/getuserinfobyusername$','main.views.Render_API_GetUserInfoByUsername'),

    #Testing page
    url(r'^apitest$','main.views.Render_APITest'),
    url(r'hello','main.views.Render_Hello'),
)
=======
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mineclass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #API: user
    url(r'^api/createuser$','main.views.Render_API_CreateUser'),
    url(r'^api/updateselfinfo$','main.views.Render_API_UpdateSelfInfo'),
    url(r'^api/login$','main.views.Render_API_Login'),
    url(r'^api/logout$','main.views.Render_API_Logout'),
    url(r'^api/getuserinfo$','main.views.Render_API_GetUserInfo'),
    url(r'^api/getuserinfobyusername$','main.views.Render_API_GetUserInfoByUsername'),

    #Testing page
    url(r'^apitest$','main.views.Render_APITest'),
)
>>>>>>> 62eaae239e1b1b1771d0813d39f397efa0fdca60

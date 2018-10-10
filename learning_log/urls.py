"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import LoginView

LoginView.template_name='users/login.html'

from learning_logs import views
from users import views as us_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

]

urlpatterns+=[
	#定义learning_logs应用的URL映射,r后面是正则表达式
	url(r'^$', views.index, name="index"),
    url(r'^topics$',views.topics,name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name="topic"),
    url(r'^new_topic$',views.new_topic,name='new_topic'),
	url(r'^new_entry/(?P<topic_id>\d+)$',views.new_entry,name='new_entry'),
	url(r'edit_entry/(?P<entry_id>\d+)$',views.edit_entry,name="edit_entry"),

    url(r'^test$', views.test, name="test"),

]

urlpatterns+=[
	#定义users应用的URL映射
	url(r'^users/login$', LoginView.as_view(),name='login'),#使用django默认提供的登录视图
	url(r'^users/logout$',us_views.logout_view,name='logout'),
	url(r'^users/register$',us_views.register,name='register'),
]
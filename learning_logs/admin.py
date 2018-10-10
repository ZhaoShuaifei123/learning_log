from django.contrib import admin

# Register your models here.

#向管理网站注册Topic模型
from learning_logs.models import Topic,Entry
admin.site.register(Topic) #让Django通过管理网站管理模型，就是显示在网站上
admin.site.register(Entry)



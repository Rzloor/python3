# 全局路由配置
from django.contrib import admin
from django.urls import path
# from App import views
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^App/', include('App.urls')),
]
# !/usr/bin/env python
# _*_ coding:utf-8 _*_


from django.conf.urls import url

from apps.users import views

urlpatterns = [
    #     1. 注册页面
    url(r'^register/$', views.RegisterView.as_view())
]

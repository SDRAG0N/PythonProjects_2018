"""PlaneTicket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from buyTicket import views
from django.conf.urls import url
from buyTicket import forms


urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'', views.index, name='index'),

    # 跳转登录界面
    url(r'^login/$', views.login),

    # 登录处理函数跳转
    url(r'^login_action/$', forms.login_action),

    # 跳转注册页面
    url(r'^userRegister/$', views.user_register),
    url(r'^travelAgencyRegister/$', views.travel_register),

    # 注册处理
    url(r'^userRegister_action/$', forms.userRegister_action),
    url(r'^travelAgencyRegister_action/$', forms.travelAgencyRegister_action),

    # 个人中心
    url(r'^myMessages/$', views.myMessages),
    # 修改个人信息
    url(r'^modifyInformation/$', forms.modifyInformation),

    # 我的订单
    url(r'^myTickets/$', views.myTickets),

    # 跳转航班信息页面
    # url(r'^queryTickets.html/$', forms.userRegister_action),

    # 航班查询
    url(r'^queryFlight/$', forms.queryFlight),

    # 订票
    url(r'^buyTicket/$', forms.buyTicket),

    # 购票
    url(r'^payTicket/$', forms.payTicket),

    # 添加航班或者删除航班
    url(r'^addOrReduce/$', forms.addOrReduce),

]

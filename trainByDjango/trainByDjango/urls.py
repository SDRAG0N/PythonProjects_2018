"""trainByDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include  # 后加

import trainByDjango.train.views as bv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', bv.index),
    url(r'^login/$', bv.login),
    # url(r'^login/action/$', bv.login_action,name='login_action'),
    url(r'^login_action/$', bv.login_action),
    url(r'^salesman_login/$', bv.salesman_login),
    url(r'^salesman_login_action/$', bv.salesman_login_action),
    url(r'^salesman/$', bv.salesman),
    url(r'^refund/$', bv.refund),
    url(r'^refund_action/$', bv.refund_action),
    url(r'^refund_action2/$', bv.refund_action2),
    url(r'^register/$', bv.register),
    url(r'^register_action/$', bv.register_action),
    url(r'^space_ticket/$', bv.space_ticket),
    url(r'^space_ticket_action/$', bv.space_ticket_action),
    url(r'train_imformation/$', bv.train_imformation),
    url(r'^Ticket_purchase/$', bv.Ticket_purchase),
    # url(r'^Ticket_purchase/action/$', bv.Ticket_purchase_action,name="Ticket_purchase_action"),
    url(r'^Ticket_purchase_action/$', bv.Ticket_purchase_action),
    url(r'^train/$', bv.train),

    url(r'^api/', include())

]

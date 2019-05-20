from django.shortcuts import render
# from buyTicket.models import user,travelagency,administrator
from . import models

# Create your views here.
from .mysql_view_models import userTicketView

# 首页
def index(request):
    return render(request, "login.html")


# 跳转登录页
def login(request):
    return render(request, "login.html")


# 跳转用户注册页
def user_register(request):
    return render(request, "userRegister.html")


# 跳转到旅行社注册页
def travel_register(request):
    return render(request, "travelAgencyRegister.html")


# 跳转个人中心
def myMessages(request):
    username = request.session.get('key', '')  # 获取登录信息
    if username:
        return render(request, "myMessage.html", {"user": username})
    else:
        return render(request, 'login.html', {"error": "请登录"})


# 跳转我的订单
def myTickets(request):
    username = request.session.get('key', '')  # 获取登录信息
    if username:
        # 视图查询
        myFlight_list = userTicketView.objects.all().filter(username=username)
        return render(request, "myTickets.html", {"myFlight": myFlight_list, "user": username})
    else:
        return render(request, 'login.html', {"error": "请登录"})


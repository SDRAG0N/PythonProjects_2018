# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict

from . import models


# Create your views here.
def index(request):
    return render(request, 'Index.html')


def space_ticket(request):
    # a=models.traffic_information.objects.all()
    return render(request, 'space_ticket.html')


def space_ticket_action(request):
    start_place = request.POST.get('start_place')
    aim_place = request.POST.get('aim_place')
    if start_place == "北京":
        if aim_place == "石家庄":
            b = models.space.objects.get(aim_station=start_place)
            # b.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            aa = min(x, y)
            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        elif aim_place == "郑州":
            b = models.space.objects.get(aim_station=start_place)
            # b.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            d = models.space.objects.get(aim_station="石家庄")
            # d.tickets
            z = d.tickets
            aa = min(x, y, z)
            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        elif aim_place == "武汉":
            b = models.space.objects.get(aim_station=start_place)
            # b.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            d = models.space.objects.get(aim_station="石家庄")
            # d.tickets
            z = d.tickets
            e = models.space.objects.get(aim_station="郑州")
            # e.tickets
            w = e.tickets
            aa = min(x, y, z, w)
            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        elif aim_place == "长沙":
            b = models.space.objects.get(aim_station=start_place)
            # b.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            d = models.space.objects.get(aim_station='石家庄')
            # d.tickets
            z = d.tickets
            e = models.space.objects.get(aim_station='郑州')
            # e.tickets
            w = e.tickets
            f = models.space.objects.get(aim_station='武汉')
            # f.tickets
            v = f.tickets
            aa = min(x, y, z, w, v)

            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        else:
            return render(request, 'space_ticket.html', {'error': '您的输入有误！！本次列车从 北京 出发依次经过石家庄、郑州、武汉最终到达长沙，请检查您的输入信息！'})
    elif start_place == "石家庄":
        if aim_place == "郑州":
            b = models.space.objects.get(aim_station=start_place)
            # b.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            aa = min(x, y)
            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        elif aim_place == "武汉":
            b = models.space.objects.get(aim_station=start_place)
            # b.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            d = models.space.objects.get(aim_station="郑州")
            # d.tickets
            z = d.tickets
            aa = min(x, y, z)
            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        elif aim_place == "长沙":
            b = models.space.objects.get(aim_station=start_place)
            # b.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            d = models.space.objects.get(aim_station="郑州")
            # d.tickets
            z = d.tickets
            e = models.space.objects.get(aim_station="武汉")
            # e.tickets
            w = e.tickets
            aa = min(x, y, z, w)
            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        else:
            return render(request, 'space_ticket.html', {'error': '您的输入有误！！本次列车从 北京 出发依次经过石家庄、郑州、武汉最终到达长沙，请检查您的输入信息！'})
    elif start_place == "郑州":
        if aim_place == "武汉":
            b = models.space.objects.get(aim_station=start_place)
            # b.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            aa = min(x, y)
            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        elif aim_place == "长沙":
            b = models.space.objects.get(aim_station=start_place)
            # b.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            d = models.space.objects.get(aim_station="武汉")
            # d.tickets
            z = d.tickets
            aa = min(x, y, z)
            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        else:
            return render(request, 'space_ticket.html', {'error': '您的输入有误！！本次列车从 北京 出发依次经过石家庄、郑州、武汉最终到达长沙，请检查您的输入信息！'})
    elif start_place == "武汉":
        if aim_place == "长沙":
            b = models.space.objects.get(aim_station=start_place)
            # c.tickets
            x = b.tickets
            c = models.space.objects.get(aim_station=aim_place)
            # c.tickets
            y = c.tickets
            aa = min(x, y)
            return HttpResponse(" 从 " + start_place + " 到 " + aim_place + " 还有" + str(aa) + "张票")
        else:
            return render(request, 'space_ticket.html', {'error': '您的输入有误！！本次列车从 北京 出发依次经过石家庄、郑州、武汉最终到达长沙，请检查您的输入信息！'})
    else:
        return render(request, 'space_ticket.html', {'error': '您的输入有误！！本次列车从 北京 出发依次经过石家庄、郑州、武汉最终到达长沙，请检查您的输入信息！'})


def train_imformation(request):
    a = models.traffic_information.objects.all()
    return render(request, 'train_imformation.html', {'space_ticket': a})


def login(request):
    return render(request, 'login.html')


def login_action(request):
    # if request.method == 'POST':
    username = request.POST.get('username', '')
    passwd = request.POST.get('passwd', '')
    user = models.users.objects.filter(name=username, passwords=passwd)
    if user:
        # request.session['user']=username
        return render(request, 'train.html')
    else:
        return render(request, 'login.html', {'error': 'username or password error!'})


def salesman_login(request):
    return render(request, 'login_admin.html')


def salesman_login_action(request):
    username = request.POST.get('username', '')
    passwd = request.POST.get('passwd', '')
    user = models.salesman.objects.filter(id=username, name=passwd)
    if user:
        # request.session['user']=username
        return render(request, 'salesman.html')
    else:
        return render(request, 'login_admin.html', {'error': 'username or password error!'})


def salesman(request):
    username = request.POST.get('username', '')
    user_imformation = models.user_ticket.objects.filter(user_id=username)
    if user_imformation:
        return render(request, 'refund2.html', {'success_ticket': user_imformation})
    else:
        return render(request, 'salesman.html', {'error': '不存在该顾客的购票记录！或者身份证输入有误请重新输入'})


def register(request):
    return render(request, 'register.html')


def register_action(request):
    username = request.POST.get('username')
    pass1 = request.POST.get('pass1')
    pass2 = request.POST.get('pass2')
    user_id = request.POST.get('user_id')
    telphone = request.POST.get('telphone')
    if username and pass1 and pass2 and user_id and telphone:
        try:
            models.users.objects.get(name=username)
            models.users.objects.get(user_id=user_id)
            return render(request, 'register.html', {'error': '该用户名已存在或者身份证已注册，注册失败！！'})
        except Exception as e:
            if pass1 == pass2:
                models.users.objects.create(user_id=username, passwords=pass1, name=username, telphone=telphone)
                return render(request, 'train.html')
            else:
                return render(request, 'register.html', {'error': 'Two inputted password inconsistencies!'})

    else:
        return render(request, 'register.html', {'error': '账号、密码、身份证号码、手机号都不能为空'})


def Ticket_purchase(request):
    return render(request, 'Ticket_purchase.html')


def Ticket_purchase_action(request):
    # if request.method == 'POST':
    start_place = request.POST.get('start_place')
    aim_place = request.POST.get('aim_place')
    id = request.POST.get('user_id')
    if id:
        try:
            b = models.space.objects.get(aim_station=aim_place)
            a = b.tickets
            if a > 0:
                models.user_ticket.objects.create(user_id=id, start_station=start_place, aim_station=aim_place)
                # g = models.space.objects.get(aim_station=aim_place)
                # h = models.space.objects.get(aim_station=start_place)
                # g.tickets = g.tickets - 1
                # g.save()
                # h.tickets = h.tickets - 1
                # h.save()
                c = models.user_ticket.objects.filter(user_id=id)
                return render(request, 'purchase_success.html', {'success_ticket': c})
                # return HttpResponse("购买成功")
            elif a == 0:
                return render(request, 'Ticket_purchase.html', {'error': '该行程票已售空!'})
            else:
                return HttpResponse("系统错误，请联系管理人员！！！")
        except Exception as e:
            return render(request, 'Ticket_purchase.html', {'error': '不存在该行程!！'})
    else:
        return render(request, 'Ticket_purchase.html', {'error': '身份证号码不能为空!'})


def purchase_success(request):
    return render(request, 'purchase_success.html')


def refund(request):
    return render(request, 'refund.html')


def refund_action(request):
    try:
        username = request.POST.get('username')
        c = models.user_ticket.objects.filter(user_id=username)
        return render(request, 'refund2.html', {'success_ticket': c})
    except Exception as e:
        return render(request, 'refund.html', {'error': '该身份证号码未有购票记录！！'})


def refund_action2(request):
    try:
        username = request.POST.get('username')
        # b=models.user_ticket.objects.get(user_id=username)
        # start_place=b.start_station
        # aim_place=b.aim_station
        # g = models.space.objects.get(aim_station=aim_place)
        # h = models.space.objects.get(aim_station=start_place)
        # g.tickets = g.tickets + 1
        # g.save()
        # h.tickets = h.tickets + 1
        # h.save()
        a = models.user_ticket.objects.filter(user_id=username).delete()
        return HttpResponse("退票成功！！！")
    except Exception as e:
        return HttpResponse("退票失败！！！")


def train(request):
    a = models.traffic_information.objects.all()
    return render(request, 'trian.html')

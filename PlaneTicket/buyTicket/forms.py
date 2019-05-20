# 非Django生成，表单处理逻辑
from . import models
from django.shortcuts import render
from .mysql_view_models import userTicketView
from django.db.models import Sum

# 登录处理
def login_action(request):
    username = request.POST.get("username", "")
    passwd = request.POST.get("passwd", "")
    if "userLogin" in request.POST:
        user = models.user.objects.filter(username=username, password=passwd)
        if user:
            request.session['key'] = username  # 登录信息存入会话
            flight_list = models.flight.objects.all()
            return render(request, "queryTickets.html", {"user": username, 'flight_list': flight_list})
        else:
            return render(request, "login.html", {'error': 'username or password error!'})
    elif "travelLogin" in request.POST:
        user = models.travelagency.objects.filter(No=username, password=passwd)
        if user:
            request.session['key'] = username
            # request.session['userClass'] = "travel"
            flight_list = models.flight.objects.all()
            return render(request, "queryTickets.html", {'flight_list': flight_list, 'user': username})
        else:
            return render(request, "login.html", {'error': 'username or password error!'})
    elif "airlineCompanyLogin" in request.POST:
        user = models.administrator.objects.filter(username=username, passwd=passwd)
        if user:
            request.session['key'] = username
            # 计算总座位
            seatsSum = models.flight.objects.all().aggregate(seatsSum=Sum('seats'))
            seatsSum2 = seatsSum['seatsSum']
            # 计算已订购座位
            seatsUser = models.userTicket.objects.all().aggregate(seatsUser=Sum('seats'))
            seatsUser2 = seatsUser['seatsUser']
            AttendanceRate = float(seatsUser2/seatsSum2)
            return render(request, "admin.html", {"user": username, "AttendanceRate": AttendanceRate})
        else:
            return render(request, "login.html", {'error': 'username or password error!'})


# 用户注册处理
def userRegister_action(request):
    username = request.POST.get('username')
    passwd1 = request.POST.get('passwd1')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    ID = request.POST.get('ID')
    phone = request.POST.get('phone')
    try:
        if models.user.objects.filter(ID=ID):
            return render(request, 'userRegister.html', {'error': '身份证已被注册，注册失败！！'})
        else:
            models.user.objects.create(ID=ID, username=username, password=passwd1, name=name, sex=sex, phone=phone)
            return render(request, "login.html", {'error': "注册成功请登录！"})
    except Exception as e:
        print(e)


# 旅行社注册
def travelAgencyRegister_action(request):
    No = request.POST.get('ID')
    password = request.POST.get('passwd1')
    name = request.POST.get('name')
    officeAddress = request.POST.get('officeAddress')
    phone = request.POST.get('phone')
    try:
        if models.travelagency.objects.filter(No=No):
            return render(request, 'travelAgencyRegister.html', {'error': '旅行社代号已被注册，注册失败！！'})
        else:
            models.travelagency.objects.create(No=No, password=password, name=name, officeAddress=officeAddress, phone=phone)
            return render(request, "login.html", {'error': "注册成功请登录！"})
    except Exception as e:
        print(e)


# 修改个人信息
def modifyInformation(request):
    username = request.session.get('key', '')
    password = request.POST.get("password")
    name = request.POST.get("name")
    sex = request.POST.get("sex")
    phone = request.POST.get("phone")
    models.user.objects.filter(username=username).update(password=password, name=name, sex=sex, phone=phone)
    return render(request, 'myMessage.html', {"message": "修改信息成功", "user": username})


# 航班查询
def queryFlight(request):
    username = request.session.get('key', '')
    startCity = request.POST.get("startCity")
    arriveCity = request.POST.get("arriveCity")
    flight_list = models.flight.objects.filter(startCity=startCity, arriveCity=arriveCity)
    if flight_list:
        return render(request, "queryTicket.html", {"user": username, 'flight_list': flight_list})
    else:
        return render(request, "queryTickets.html", {"user": username, 'error': "对不起，没有该航班"})


# 订票
def buyTicket(request):
    username = request.session.get('key', '')
    flightId = request.POST.get("flightId")
    seats = models.flight.objects.filter(flightId=flightId).values("seats")
    # 取值
    seat = seats.first()['seats']
    if seat > 0:
        models.flight.objects.filter(flightId=flightId).update(seats=seat-1)
        # 判断用户是否已有此订单
        userSeat = models.userTicket.objects.filter(flightId=flightId).values("seats")
        if userSeat:
            uS = userSeat.first()['seats']
            # 如果已存在订单则座位数加1
            models.userTicket.objects.filter(flightId=flightId, username=username).update(seats=uS+1)
        else:
            models.userTicket.objects.create(flightId=flightId, username=username, seats=1)
        # 此航班是肯定存在的
        flight_list = models.flight.objects.all()
        return render(request, "queryTickets.html", {"user": username, 'message': "您购买的机票已加入订单，请前往我的订单付款，或继续购票", 'flight_list': flight_list})
    else:
        return render(request, "queryTickets.html", {"user": username, "message": "剩余票数不足"})


# 购票
def payTicket(request):
    username = request.session.get('key', '')
    userTicketsId = request.POST.get("userTicketsId")
    # 只删匹配到的第一条
    seats = models.userTicket.objects.filter(username=username, userTicketsId=userTicketsId).values("seats")
    seatInt = seats.first()['seats']
    if seatInt==1:
        # seatInt = seats.first()['seats']
        models.userTicket.objects.filter(username=username, userTicketsId=userTicketsId).delete()
    else:
        models.userTicket.objects.filter(username=username, userTicketsId=userTicketsId).update(seats=seatInt-1)
    myFlight_list = userTicketView.objects.all().filter(username=username)
    # 显示我的订单
    return render(request, "myTickets.html", {"message": "付款成功", "myFlight": myFlight_list, "user": username})


# 管理员添加或者删除航班
def addOrReduce(request):
    username = request.session.get('key', '')
    if "add" in request.POST:
        flightId = request.POST.get("flightId")  # 航班号
        flightName = request.POST.get("flightName")  # 航班名
        flightType = request.POST.get("flightType")  # 飞机型号
        flightCompany = request.POST.get("flightCompany")  # 航空公司
        startTime = request.POST.get("startTime")  # 起飞时间
        arriveTime = request.POST.get("arriveTime")  # 到达时间
        startCity = request.POST.get("startCity")  # 起飞城市
        arriveCity = request.POST.get("arriveCity")  # 到达城市
        flyTime = request.POST.get("flyTime")  # 飞行时间（礼拜一到礼拜日的选择）
        seats = request.POST.get("seats")  # 剩余座位数
        fare = request.POST.get("fare")  # 票价
        discountRate = request.POST.get("discountRate")  # 折扣比率
        if models.flight.objects.filter(flightId=flightId):
            return render(request, "admin.html", {"user": username, "message": "该航班已存在，添加失败"})
        else:
            models.flight.objects.create(flightId=flightId, flightName=flightName, flightType=flightType,flightCompany=flightCompany, startTime=startTime, arriveTime=arriveTime, startCity=startCity, arriveCity=arriveCity, flyTime=flyTime, seats=seats, fare=fare, discountRate=discountRate)
            return render(request, "admin.html", {"user": username, "message": "添加成功！"})
    elif "reduce" in request.POST:
        reduceFlightId = request.POST.get("reduceFlightId")
        user = models.flight.objects.filter(flightId=reduceFlightId)
        if user:
            models.flight.objects.filter(flightId=reduceFlightId).delete()
            return render(request, "admin.html", {'user': username, 'message': "删除航班成功"})
        else:
            return render(request, "admin.html", {'message': '该航班不存在，看清楚再删好不好'})
    elif "setRate" in request.POST:
        setFlightId = request.POST.get("setFlightId")
        setFlightRate = request.POST.get("setFlightRate")
        flightIdSet = models.flight.objects.filter(flightId=setFlightId)
        if flightIdSet:
            models.flight.objects.filter(flightId=setFlightId).update(discountRate=setFlightRate)
            return render(request, "admin.html", {'user': username, 'message': "设置折扣率成功"})
        else:
            return render(request, "admin.html", {'message': '该航班不存在，看清楚再设置好不好'})

from __future__ import unicode_literals

from django.db import models


# Create your models here.
class user(models.Model):
    ID = models.CharField(max_length=18, primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)


class travelagency(models.Model):
    No = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    officeAddress = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)


class administrator(models.Model):
    username = models.CharField(max_length=50)
    passwd = models.CharField(max_length=100)


class flight(models.Model):
    flightId = models.CharField(max_length=10)  # 航班号
    flightName = models.CharField(max_length=20)  # 航班名
    flightType = models.CharField(max_length=20)  # 飞机型号
    flightCompany = models.CharField(max_length=20)  # 航空公司
    startTime = models.CharField(max_length=20)  # 起飞时间
    arriveTime = models.CharField(max_length=20)  # 到达时间
    startCity = models.CharField(max_length=20)  # 起飞城市
    arriveCity = models.CharField(max_length=20)  # 到达城市
    flyTime = models.CharField(max_length=20)  # 飞行时间（礼拜一到礼拜日的选择）
    seats = models.IntegerField()  # 剩余座位数
    fare = models.CharField(max_length=20)  # 票价
    discountRate = models.CharField(max_length=20)  # 折扣比率


class userTicket(models.Model):
    userTicketsId = models.IntegerField(primary_key=True)
    flightId = models.CharField(max_length=10, null=True)  # 航班号
    username = models.CharField(max_length=18, null=True)  # 身份证 或者 旅行社号
    seats = models.IntegerField()

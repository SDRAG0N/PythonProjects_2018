from .models import *

class userTicketView(models.Model):
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
    userTicketsId = models.IntegerField(primary_key=True)  # 订单号
    flightId = models.CharField(max_length=10, null=True)  # 航班号
    seats = models.IntegerField()
    username = models.CharField(max_length=18, null=True)  # 身份证 或者 旅行社号

    class Meta:
        db_table = 'userTicketView'


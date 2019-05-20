# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class traffic_information(models.Model):
    trafic_id = models.CharField(max_length=20, default='c001')
    start_station = models.CharField(max_length=20)
    aim_station = models.CharField(max_length=20)
    start_time = models.CharField(max_length=20)
    aim_time = models.CharField(max_length=20)
    train_type = models.CharField(max_length=20)
    mileage = models.CharField(max_length=20)


class users(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    passwords = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    telphone = models.IntegerField()


class space(models.Model):
    aim_station = models.CharField(max_length=20, primary_key=True)
    tickets = models.IntegerField()


class user_ticket(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    start_station = models.CharField(max_length=20)
    aim_station = models.CharField(max_length=20)


class salesman(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)


class salesman(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)

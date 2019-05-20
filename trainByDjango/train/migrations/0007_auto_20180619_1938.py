# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0006_auto_20180619_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='tickets',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='telphone',
            field=models.IntegerField(),
        ),
    ]

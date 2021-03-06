# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20170311_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountType', models.CharField(choices=[('cash', '现金'), ('rice', '米粒')], max_length=50, verbose_name='账户类型')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='余额')),
                ('createdTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatedTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feedback', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='feedback',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.FeedBack', verbose_name='打卡信息'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0020_activity_istop'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='zeroableMily',
            field=models.IntegerField(default=0, verbose_name='活动赠米'),
        ),
    ]
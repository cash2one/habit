# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_remove_orgactivityhistory_getmily'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgactivityhistory',
            name='activityDays',
            field=models.IntegerField(default=0, verbose_name='持续天数'),
        ),
    ]

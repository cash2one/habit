# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0019_auto_20170305_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='isTop',
            field=models.BooleanField(default=False, verbose_name='是否置顶'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0006_auto_20170324_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='childpwd',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0018_activity_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='memo',
            field=models.TextField(max_length=2048, verbose_name='注意事项'),
        ),
    ]
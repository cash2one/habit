# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20170404_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='classgroup',
            name='imgUrl',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20170312_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysaccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=20, verbose_name='余额'),
        ),
    ]
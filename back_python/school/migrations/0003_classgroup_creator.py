# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 00:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0002_auto_20170123_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='classgroup',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, verbose_name='编码')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('createdTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatedTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('level', models.CharField(choices=[('L', '低'), ('M', '中'), ('H', '高')], max_length=4, verbose_name='难度')),
            ],
            options={
                'verbose_name_plural': '习惯',
                'verbose_name': '习惯',
            },
        ),
        migrations.CreateModel(
            name='HabitCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, verbose_name='编码')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('createdTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatedTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': '习惯分类',
                'verbose_name': '习惯分类',
            },
        ),
        migrations.AddField(
            model_name='habit',
            name='habitCatalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitinfo.HabitCatalog', verbose_name='所属分类'),
        ),
    ]

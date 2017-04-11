# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20170323_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounthistory',
            name='tradeType',
            field=models.CharField(choices=[('fee', '套餐服务费'), ('deposit', '押金'), ('milyOutput', '米粒打赏'), ('milyOutputByDonate', '米粒捐赠'), ('feedBackMilyInput', '打卡奖励米粒'), ('feedBackReturnDeposit', '打卡返还押金'), ('aveDeposit', '平均分配懒人押金'), ('takeCash', '用户提现')], max_length=50, verbose_name='类型'),
        ),
    ]

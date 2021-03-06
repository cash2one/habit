# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20170312_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounthistory',
            name='tradeDate',
            field=models.DateTimeField(auto_now=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='accounthistory',
            name='tradeType',
            field=models.CharField(choices=[('fee', '套餐服务费'), ('deposit', '押金'), ('milyInput', '套餐囤米'), ('freeMilyInput', '免费的套餐'), ('milyInputByDeposit', '押金囤米'), ('milyOutput', '米粒打赏'), ('milyOutputByDonate', '米粒捐赠'), ('feedBack', '打卡奖励米粒'), ('feedBackReturnDeposit', '打卡返还押金'), ('aveDeposit', '平均分配懒人押金'), ('takeCash', '用户提现')], max_length=50, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='sysaccounthistory',
            name='tradeDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='sysaccounthistory',
            name='tradeType',
            field=models.CharField(choices=[('sysFillMily', '平台生产米粒'), ('sysFreeOutMily', '平台免费赠送米粒'), ('sysFreeInputMily', '平台免费赠送退回米粒'), ('sysTakeCash', '平台提现'), ('sysInitCash', '平台预存')], max_length=50, verbose_name='类型'),
        ),
    ]

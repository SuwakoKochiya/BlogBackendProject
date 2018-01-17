# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-12 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0007_auto_20180104_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postbaseinfo',
            name='browse_password',
            field=models.CharField(blank=True, help_text='浏览密码', max_length=20, null=True, verbose_name='浏览密码'),
        ),
        migrations.AlterField(
            model_name='postbaseinfo',
            name='browse_password_encrypt',
            field=models.CharField(blank=True, help_text='浏览密码加密', max_length=100, null=True, verbose_name='浏览密码加密'),
        ),
    ]
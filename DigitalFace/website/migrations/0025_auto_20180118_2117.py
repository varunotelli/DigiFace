# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_auto_20180118_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='UID',
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
    ]

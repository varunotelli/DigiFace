# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_auto_20180118_2117'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='temp',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='temp',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0016_auto_20180118_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('DOB', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('DOB', models.DateField()),
            ],
        ),
    ]

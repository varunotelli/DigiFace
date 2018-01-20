# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20180118_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('Name', models.CharField(max_length=250)),
                ('DOB', models.DateField()),
                ('Street', models.CharField(max_length=250)),
                ('Locality', models.CharField(max_length=250)),
                ('City', models.CharField(max_length=250)),
                ('District', models.CharField(max_length=250)),
                ('State', models.CharField(max_length=250)),
                ('Pincode', models.BigIntegerField()),
                ('UID', models.CharField(max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Persons',
        ),
    ]

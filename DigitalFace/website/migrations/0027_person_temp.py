# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0026_auto_20180118_2120'),
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
                ('Pincode', models.CharField(max_length=8)),
                ('UID', models.CharField(max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('DOB', models.DateField()),
                ('Street', models.CharField(max_length=250, null=True)),
                ('Locality', models.CharField(max_length=250, null=True)),
                ('City', models.CharField(max_length=250, null=True)),
                ('District', models.CharField(max_length=250, null=True)),
                ('State', models.CharField(max_length=250, null=True)),
                ('Pincode', models.CharField(max_length=8, null=True)),
                ('UID', models.CharField(max_length=250, null=True, unique=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='City',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='temp',
            name='District',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='temp',
            name='Locality',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='temp',
            name='Pincode',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='temp',
            name='State',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='temp',
            name='Street',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='temp',
            name='UID',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
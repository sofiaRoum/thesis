# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-19 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20170119_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='home_address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_numer',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-23 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0006_auto_20170105_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='image',
            field=models.ImageField(blank=True, upload_to='bike_image'),
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, upload_to='car_image'),
        ),
    ]
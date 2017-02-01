# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-25 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0008_auto_20170125_1717'),
        ('hotels', '0004_room_price'),
        ('booking', '0007_bookroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookBike',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('hotels.room',),
        ),
        migrations.CreateModel(
            name='BookCar',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('rentals.car',),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_auto_20161128_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='cc',
            field=models.CharField(choices=[('1000', '1000'), ('1100', '1100'), ('1300', '1300'), ('1600', '1600'), ('2000', '2000')], default='', max_length=200),
        ),
    ]

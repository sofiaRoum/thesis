# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-05 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_auto_20161209_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='cc',
            field=models.CharField(max_length=50),
        ),
    ]

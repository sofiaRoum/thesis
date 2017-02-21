# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-02 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0009_auto_20170202_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='bike_image')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rentals.Bike')),
            ],
        ),
    ]
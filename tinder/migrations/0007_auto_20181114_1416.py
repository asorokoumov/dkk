# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0006_car_assessor_resolution'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_url2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='image_url3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='image_url4',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

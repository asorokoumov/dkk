# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0005_auto_20181113_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='assessor_resolution',
            field=models.CharField(default='success', max_length=200),
            preserve_default=False,
        ),
    ]

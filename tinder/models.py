# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Car(models.Model):
    image_url = models.CharField(max_length=200)
    defect = models.CharField(max_length=200)


class User(models.Model):
    login = models.CharField(max_length=200)

    def __str__(self):
        return self.login


class QualityCheck(models.Model):
    user = models.CharField(max_length=200)
    car = models.ForeignKey(Car)
    resolution = models.BooleanField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.user + ' ' + self.car.image_url



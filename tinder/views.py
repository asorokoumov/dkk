# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from tinder.models import Car, QualityCheck, User


# Create your views here.
def index(request):
    if request.method == "POST":
        login = request.POST.get('username', '')
        if not User.objects.filter(login=login).exists():
            user = User(login=login)
            user.save()
            return redirect('dkk', user)
        else:
            return render(request, 'tinder/login.html', {'login_error': 'Похоже, вы уже проходили опрос'})
    else:
        return render(request, 'tinder/login.html')


def dkk(request, user):
    if not User.objects.filter(login=user).exists():
        return redirect('index')

    cars = Car.objects.all()
    return render(request, 'tinder/index.html', {'cars': cars})


def thankyou(request, user):
    return render(request, 'tinder/thankyou.html')


def like(request, user, car):
    car = Car.objects.get(id=car)
    quality_check = QualityCheck(user=user, car=car, resolution=False)
    quality_check.save()
    return HttpResponse("OK")


def dislike(request, user, car):
    car = Car.objects.get(id=car)
    quality_check = QualityCheck(user=user, car=car, resolution=True)
    quality_check.save()
    return HttpResponse("OK")

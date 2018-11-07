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


def result(request):
    quality_checks = QualityCheck.objects.all()
    cars = []
    for qc in quality_checks:
        if qc.car not in cars:
            cars.append(qc.car)
    result = []
    for car in cars:
        total = QualityCheck.objects.filter(car=car).count()
        passed = QualityCheck.objects.filter(car=car, resolution=True).count()
        result.append([car, float(passed)/float(total)*100, 100-float(passed)/float(total)*100, passed, total-passed])
    return render(request, 'tinder/result.html', {'result': result})


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


def upload_cars (request):
    cars = [['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/225847/62c149f87c404418b1aeb2befb171448.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/925941/3edf8578f3ec4137a9a3492c5c1f7777.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/759543/4f0c2f709a4f47de988e51dfe102ff51.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/918663/c0d7be34bffd4f6a997ab8357b4e87f4.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1328725/ac96b00b67874e739be2b0ff7c105ee6.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/986133/54ae0c929b874d3a8edc827b3800f400.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/986133/8f8e912bcdda41728982b0eed3752a6d.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/773375/3390fc0864ae4b319e208ab63ba49040.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1367673/5ce0a1686a874acd8fbf8ed18444d1b9.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/361841/0642be1192384f4eb9223b585d2667d6.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/986133/19b485dfb09f4f2887d741ea0aba5cef.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/918663/c30c0bf155d6438ba10880c5f27c39bf.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/918663/e26e06d8eebb4c89876cb163daf22ff0.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1242879/80792513c17342d1a0e325dc22332832.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1100895/450feca9ad6e42359d096bc06fbc109e.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/918663/ab166a270e0f4931bba58b03e5c68ce9.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/479912/9110f4c91c6c474e849992f00d960589.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/741827/f0192c3296a44c669115b361a48a06f2.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/741827/ade0c84443b7443da0a775c1b37847ab.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/986133/e823359782b54c23b2f2d721ad4b513b.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1367673/f21f9173a503468f80ac04d82d975b78.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/773375/b84e24bba3704f0fa0381ac6af6cdb22.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/479912/60a3b1d48a33480c833a3eb6aa997be2.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1221495/c7294c290eb24b26b53d5a3021cd1353.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1221495/663fcc0fe8d9474fba552a806cb7c6f8.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/398905/686d260017514537a4602b05d16b570c.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1341193/88e2e720a9bf40c1befc32d156eea2e7.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1328725/342fa3101d4a4a79ae376b6259841af4.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1341193/769d7f43000d4f9db1950b363a09bf5a.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/741827/35afca99aa6744e6a11826773a55f337.jpg']]
    for car in cars:
        load_car = Car(image_url=car[2], defect=car[0], details=car[1])
        load_car.save()
    return HttpResponse("OK")

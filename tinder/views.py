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


def upload_cars (request):
    cars = [['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/759543/3063c2e9a9c448cdb88ad63c4191d829.jpg'],
['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/225847/a6bb7e75a1274af9aa14450840e470a9.jpg'],
['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/759543/2d36683a1d004958af5d2fe5f83505a9.jpg'],
['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/918663/7e4dc0f604c5419f9f5dcd401f6941e2.jpg'],
['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1100895/154f540adc7c4ac48c51307ae8c3a4de.jpg'],
['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1367673/8052f5e15b2a45b1ab512fa1390fb2f1.jpg'],
['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1100895/e1d18dfefab4426c8b92b739ee64dc1a.jpg'],
['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/925941/2e5e0b5b5d1c4ddbba77dfa4d3642ea0.jpg'],
['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/773375/336eb8a111de47079d61f3f3745ecfde.jpg'],
['повреждение', 'нет заднего бампера', 'https://storage.mds.yandex.net/get-taximeter/925941/ffea0a9c9f7141c88bb68090da07a67e.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1100895/d3d741fbcbc14f08b1d301032fa5cd0d.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1100895/ca1a460df3934f30be4f7f021149ec6b.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1328725/c13a0d1eef404390945446681d75896b.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1100895/ca1a460df3934f30be4f7f021149ec6b.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1367673/da36b3467c9c4fba92dfc220c0fbf627.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1100895/338c2566d88440e2aa850ca2ca5d2761.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/986133/223bc04a064e45f9ad129a1d75f0fb5e.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/1221495/c5510336051e4c89857606af61e55266.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/479912/22308c86a146434b90dd3d2a276d855b.jpg'],
['повреждение', 'нет переднего бампера', 'https://storage.mds.yandex.net/get-taximeter/925941/c59532f0f48b4d3ca7ac7e70325c7933.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/1221495/b95b33e40d684e3e93a6431c3c023f2e.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/1221495/32e0bd09761747a499084fbf3d8889d0.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/925941/d978a65788a54a949e5b7112b0bee88b.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/925941/f09a8fbd40e4424da14ec69cfa8d5208.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/1221495/76a6534458864124a358359369fd99d1.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/925941/b8958eeb5c334ca38343eb507013191e.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/1328725/e71f2c49cc7a4ed391546160d5a90234.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/1328725/d59d9b7f8ce94a22bbca2a32d51fa984.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/925941/863136615c00438ca65b4effbb33a9d2.jpg'],
['повреждение', 'большое повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/986133/98de85c47cb049eb8d83273c2d5a2311.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/986133/ae165ca19d414e15bc2d309ef1cab11f.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/986133/84ae61e3daa54594bf52b6cf46f16fda.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/986133/40e00d7df48249439eabab8a81134493.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/986133/9e4d247fbc4a431f88f90deb6a231973.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/918663/81f2825616ba4b0bbfc2fdb0934c784f.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/986133/42806d46dfbc4e92bf840542d2caeef5.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/1242879/2d459731340e4ea4ad35d1c74e86ab37.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/225847/3d6be42fa9834fa39dd496b55cbdc5b2.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/1367673/a8876c2306ea4ec9a2b78a704cf47fa6.jpg'],
['повреждение', 'большое повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/986133/b2adc2f1f56d4082a1a6230ec40518bf.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/1328725/e71f2c49cc7a4ed391546160d5a90234.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/479912/7255d64e1d4c4db5bb3e636be8d3698c.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/225847/6fb30bd681f94eb2bcb1f3165dd9a8c5.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/479912/0af6becf926d4f81ad0370d3dd931b7b.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/918663/f87a981927314444b94a4626ec48bdca.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/479912/7255d64e1d4c4db5bb3e636be8d3698c.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/1100895/e6057670be6b4b098a027252fec0b931.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/773375/56d981eaa28744f588d3b9ae92c8d2e3.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/1100895/f140f9fbe92d4a1290aaa72ba6935f71.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/479912/48feb3c5dd7a4ac9bd69dcb8571bf2fd.jpg'],
['повреждение', 'среднее повреждение сзади', 'https://storage.mds.yandex.net/get-taximeter/986133/6869d059f9fb445288c5c53017994d59.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/925941/b2b3dd2d9fa34c83a5a942acd4b16237.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/1341193/a78cde1bc6154c2c8bfafd8e3b97ef1e.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/925941/b2b3dd2d9fa34c83a5a942acd4b16237.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/925941/7329a38a8600482d85ab0399e4816375.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/741827/1b104b36ec3740fcb70e6ea3b275418f.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/925941/6bdbe9ae47b340f8b9bed59a9e70c5ea.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/1100895/f8bc2f96339a4dc586b71e6dce6c1737.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/1328725/e3ae4633d47f427cac40ce1ddfeab8c9.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/479912/3a41babbd84d4655ba1716172b53041c.jpg'],
['повреждение', 'среднее повреждение спереди', 'https://storage.mds.yandex.net/get-taximeter/1328725/a38905a55f7745ccafaa2d350043a6fb.jpg'],
['повреждение', 'отсутствует/разбира фара', 'https://storage.mds.yandex.net/get-taximeter/1341193/c30ca490262348089dfb1e22a31310ce.jpg'],
['повреждение', 'отсутствует/разбира фара', 'https://storage.mds.yandex.net/get-taximeter/741827/4c5bd33eeeea4d3bb1902d3ed51a5e91.jpg'],
['повреждение', 'отсутствует/разбира фара', 'https://storage.mds.yandex.net/get-taximeter/918663/0823c31e090a430da05ef36110415ae3.jpg'],
['повреждение', 'отсутствует/разбира фара', 'https://storage.mds.yandex.net/get-taximeter/918663/11df4529e2654b859c591f5fddc6d34e.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/225847/62c149f87c404418b1aeb2befb171448.jpg'],
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
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/988199/7f535725a83e4cf1bc44c7a773f9d7a8.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/986133/bc75ee7dda2e4bd3946e612b087bd44d.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/225847/77b32fcaa81b4b1189fed5dc6e64a07d.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1221495/67013638cca64b2ca8fb00c645e08e8b.jpg'],
['повреждение', 'небольшие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1100895/49a10b41451e4494aa87bf0067f219c4.jpg'],
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
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/741827/35afca99aa6744e6a11826773a55f337.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1328725/406df4fe4eb143ae8aa56814ab0ef077.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1341193/750e45ac90194bc7bd030c6a6589e2e8.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/918663/8e4e0818809147d0b821e98835d07b15.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/773375/027663e537f54996b28f3f88fe7d8493.jpg'],
['повреждение', 'большие повреждения на борту', 'https://storage.mds.yandex.net/get-taximeter/1221495/3c23150d69e74f8a9a6b21aeaa861fa3.jpg']]
    for car in cars:
        load_car = Car(image_url=car[2], defect=car[0], details=car[1])
        load_car.save()
    return HttpResponse("OK")

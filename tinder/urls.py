from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user>[-\w]+)/$', views.dkk, name='dkk'),
    url(r'^(?P<user>[-\w]+)/thankyou/$', views.thankyou, name='thankyou'),
    url(r'^(?P<user>[-\w]+)/like/(?P<car>[-\w]+)/$', views.like, name='like'),
    url(r'^(?P<user>[-\w]+)/disike/(?P<car>[-\w]+)/$', views.dislike, name='dislike'),

]
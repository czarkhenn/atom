from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('official-exchange/', views.ofcexchange, name='ofcexchange'),
    path('company/', views.company, name='company'),
    path('xec/', views.xec, name='xec'),
    path('xet/', views.xet, name='xet'),
    path('media/', views.media, name='media'),
    path('media/jp/', views.mediajp, name='mediajp'),
    path('media/video/', views.video, name='video'),
    path('whitelabel/', views.wlabel, name='whitelabel'),

]

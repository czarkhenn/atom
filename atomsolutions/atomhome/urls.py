from django.urls import path, include
from . import views
from .views import NewsDetailView, NewsView

app_name = 'atomhome'

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
    path('joinus/', views.recruit, name='recruit'),
    path('joinus/1/', views.dt1, name='dt1'),
    path('joinus/2/', views.dt2, name='dt2'),
    path('joinus/3/', views.dt3, name='dt3'),
    path('joinus/4/', views.dt4, name='dt4'),
    path('joinus/5/', views.dt5, name='dt5'),
    path('joinus/6/', views.dt6, name='dt6'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('faq/', views.faq, name='faq'),
    path('vr-partner/', views.vr, name='vr'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='details'),


]

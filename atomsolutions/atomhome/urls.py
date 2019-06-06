from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('official-exchange/', views.ofcexchange, name='ofcexchange'),
    path('company/', views.company, name='company'),

]

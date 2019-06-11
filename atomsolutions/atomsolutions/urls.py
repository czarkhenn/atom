from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('atom-admin/', admin.site.urls),
    path('', include('atomhome.urls')),
]

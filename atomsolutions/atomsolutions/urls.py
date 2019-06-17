from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('atom-admin/', admin.site.urls),
] 

urlpatterns += i18n_patterns(
path('', include('atomhome.urls')),

)

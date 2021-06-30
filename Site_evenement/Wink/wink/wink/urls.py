from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include #, handler404

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^murPrincipal/$',views.murPrincipal),
    url(r'register/', include('register.urls')),
    url(r'profil/', include('profil.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

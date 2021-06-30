from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include #, handler404

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   url(r'^modifProfil/$', views.modifProfil), #On considere ici que l'url commence par profil
   url(r'^$', views.Profil),
   url(r'^NouvellePhoto/$', views.NouvellePhoto),
   url(r'^CreateEvent/$', views.CreateEvent),
   url(r'^DisplayEvents/$', views.DisplayEvents),

   url(r'^Chat/idUser=(?P<idUser>[0-9]+)/$', views.Chat),

   url(r'^Attente/$', views.Attente),
   url(r'^ParticipeEvent/idEvent=(?P<idEvent>[0-9]+)/$', views.ParticipeEvent),
   url(r'^VoirProfil/idWinker=(?P<idWinker>[0-9]+)/$', views.VoirProfil),
   path('', include('django.contrib.auth.urls')),
 ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'), #perehod na glavnuyu stranichku
    path('about', views.about, name = 'about'),
    path('usings_app', views.explication, name = 'usings'),
    path('download', views.download, name = 'download'),
]
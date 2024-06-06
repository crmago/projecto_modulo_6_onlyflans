from django.urls import path
from main.views import indice, acerca, bienvenido, contacto

urlpatterns = [
    path('', indice, name=''),
    path('acerca/', acerca, name='acerca'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('contacto/', contacto, name='contacto'),
]

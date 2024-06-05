from django.urls import path
from main.views import indice, acerca, bienvenido

urlpatterns = [
    path('', indice),
    path('acerca/<int:id>/', acerca),
    path('bienvenido/', bienvenido)
]

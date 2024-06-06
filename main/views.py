from django.http import HttpResponse
from django.shortcuts import render
from main.postres import postres

# Create your views here.
def indice(req):
    context = {
        'titulo': 'Nuestros Flanes',
        'postres': postres,
    }
    return render(req, 'index.html', context)

def acerca(req):
    context = {
        'postres': postres, 
    }
    return render(req, 'about.html', context)

def bienvenido(req):
    context = {
        'postres': postres,
    }
    return render(req, 'welcome.html', context)

def contacto(req):
    context = {
        'postres': postres,
    }
    return render(req, 'form.html', context)

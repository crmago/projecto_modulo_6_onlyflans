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

def acerca(req, id):
    return render(req, 'about.html')

def bienvenido(req): 
    return render(req, 'welcome.html')

from django.shortcuts import render, redirect
from .forms import ContactFormModelForm
from main.postres import postres

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
    return render(req, 'contacto.html', context)


def contact_form(req):
    if req.method == 'POST':
        form = ContactFormModelForm(req.POST)
        if form.is_valid():
            form.save()  # Guardar el formulario en la base de datos
            return render(req, 'form_success.html')  # Redireccionar a la página de éxito si no hay errores
        else:
            errores = form.errors  # Capturar los errores del formulario
    else:
        form = ContactFormModelForm()
        errores = []

    return render(req, 'form.html', {'form': form, 'errores': errores})


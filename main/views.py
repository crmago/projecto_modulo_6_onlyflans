from django.shortcuts import redirect, render
from .models import Flan
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.views import LogoutView


def indice(req):
    # Obtener todos los flanes privados de la base de datos
    flanes = Flan.objects.filter(is_private=False)
    context = {
        'titulo': 'Nuestros Flanes',
        'flanes': flanes,
    }
    return render(req, 'index.html', context)

def acerca(req):
    
    return render(req, 'about.html')

@login_required
def bienvenido(request):
    # Obtener todos los flanes de la base de datos si es necesario
    flanes = Flan.objects.all()
    context = {
        'flanes': flanes,
    }
    return render(request, 'welcome.html', context)

def contacto(req):
    return render(req, 'contacto.html')

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

class LoginViewPropia(SuccessMessageMixin ,LoginView):
    success_message = 'Has ingresado correctamente'


class LogoutViewPropio(LogoutView):
    next_page = '/'  # Página a la que redirigir después del logout

    def dispatch(self, request, *args, **kwargs):
        # Llama al método padre (LogoutView) para realizar el logout
        response = super().dispatch(request, *args, **kwargs)

        # Muestra el mensaje de éxito usando el sistema de mensajes de Django
        messages.success(self.request, 'Has cerrado sesión correctamente.')

        return response




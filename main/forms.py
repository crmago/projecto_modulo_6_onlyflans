# forms.py
from django import forms
from .models import Contacto

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['customer_name', 'customer_email', 'message']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Mensaje'}),
        }
        labels = {
            'customer_name': 'Nombre',
            'customer_email': 'Correo electrónico',
            'message': 'Mensaje',
        }
        error_messages = {
            'customer_name': {
                'required': 'El campo Nombre es obligatorio.',
            },
            'customer_email': {
                'required': 'El campo Correo electrónico es obligatorio.',
                'invalid': 'Ingrese una dirección de correo electrónico válida.',
            },
            'message': {
                'required': 'El campo Mensaje es obligatorio.',
            },
        }

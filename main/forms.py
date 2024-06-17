# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Contacto


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'email']  # Campos que quieres incluir en el formulario

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


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

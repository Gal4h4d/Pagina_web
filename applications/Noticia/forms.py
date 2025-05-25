from django import forms
from .models import Noticia

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar contraseña'
            }),
        }

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['Titulo', 'Parrafo', 'Fecha_Publicacion', 'imagen']
        widgets = {
            'Titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el título de la noticia'
            }),
            'Parrafo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el contenido de la noticia',
                'rows': 6
            }),
            'Fecha_Publicacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

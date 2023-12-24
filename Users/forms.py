from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class UserCreationFormCustom(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label="Ingresar usuario")
    password1 = forms.CharField(label="Contraseña")
    password2 = forms.CharField(label="Repetir contraseña")

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')

    class Meta:
        model = User
        fields = ['email','username', 'last_name', 'first_name']


class ProductoFormulario(forms.Form):
    MODELOS_CHOICES = [
        ('T61', 'ThinkPad T61'),
        ('X60', 'ThinkPad X60'),
        ('X1', 'ThinkPad X1'),
        ('T480', 'ThinkPad T480'),
        ('T490', 'ThinkPad T490'),
        ('X280', 'ThinkPad X280'),
    ]
    modelo = forms.ChoiceField(choices=MODELOS_CHOICES)
    descripcion = forms.CharField()
    imagen = forms.ImageField()


class ExperienciaFormulario(forms.Form):
    mensaje = forms.CharField(widget =forms.Textarea)
    puntaje = forms.IntegerField()



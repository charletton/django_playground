from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Producto, Experiencia
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


class ProductoFormulario(forms.ModelForm):
    MODELOS_CHOICES = [
        ('T61', 'ThinkPad T61'),
        ('X60', 'ThinkPad X60'),
        ('X1', 'ThinkPad X1'),
        ('T480', 'ThinkPad T480'),
        ('T490', 'ThinkPad T490'),
        ('X280', 'ThinkPad X280'),
    ]
    modelo = forms.ChoiceField(choices=MODELOS_CHOICES)

    class Meta:
        model = Producto  # Agrega esta línea para especificar el modelo
        fields = ['modelo', 'descripcion', 'imagenProducto']
 
class ExperienciaFormulario(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['mensaje', 'puntaje']
        widgets = {
            'mensaje': forms.Textarea,
        }

    puntaje = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '10'})
    )
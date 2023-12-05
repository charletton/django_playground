from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProductoFormulario(forms.Form):
    modelo = forms.CharField()
    descripcion = forms.CharField()
    fecha_salida = forms.IntegerField()

class ExperienciaFormulario(forms.Form):
    mensaje = forms.CharField(widget =forms.Textarea)
    puntaje = forms.IntegerField()



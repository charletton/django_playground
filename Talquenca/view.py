from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from Users.forms import *
from Users.models import * 
#login + registro
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

#vistas
def index(request):
    return render(request, 'index.html')

#vistas para users (login, registrarse y logoutear)
def vista_de_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')


            user = authenticate(username= usuario, password=contrasenia)


            login(request, user)            
            return render(request, "index.html", {"mensaje": f'Bienvenido {user.username}'})

    else:
        form = AuthenticationForm()

    return render(request, "usuarios/login.html", {"form": form})

@login_required
def vista_de_edicion(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return render(request, "index.html")
    else:
        formulario = UserEditForm(instance=request.user)
    return render(request, "usuarios/edicion.html", {"miFormulario": formulario, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name= 'usuarios/contrasena.html'
    succes_url = reverse_lazy('EditarPerfil')

def vista_de_registro(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username'] 
            form.save()
            return render(request, "index.html", {"mensaje": "Usuario creado correctamente", "mensaje1": username})
        else:
            return render(request, "usuarios/registro.html", {"form": form})
    else:
        form = UserCreationFormCustom()
        return render(request, "usuarios/registro.html", {"form": form})




@login_required(login_url="login")
def vista_de_formulario_producto(request):
    if request.method == 'POST':
        nuevo_formulario = ProductoFormulario(request.POST, request.FILES)

        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data

            nuevo_producto = Producto(
                modelo=informacion['modelo'],
                descripcion=informacion['descripcion'],
                imagenProducto=request.FILES.get('imagenProducto')
            )
            nuevo_producto.save()

            messages.success(request, 'Producto creado exitosamente.')
            return render(request, 'extras/creado.html')

        # Manejar errores y mostrar mensajes
        messages.error(request, 'Error al crear el producto. Revisa los datos ingresados.')
        print(nuevo_formulario.errors)

    else:
        nuevo_formulario = ProductoFormulario()

    return render(request, 'producto/producto.html', {'formulario': nuevo_formulario})


@login_required(login_url="login")
def vista_de_formulario_experiencia(request):
    if request.method == 'POST':
        nuevo_formulario = ExperienciaFormulario(request.POST)

        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data

            nueva_experiencia = Experiencia(
                mensaje=informacion['mensaje'],
                puntaje=informacion['puntaje'],
            )
            nueva_experiencia.save()

            return render(request, 'creado.html')
    else: 
        nuevo_formulario = ExperienciaFormulario()
        return render(request, 'experiencia/experiencia.html', {'formulario': nuevo_formulario})



@login_required(login_url="login")
def editarProducto(request, producto_modelo):
    pass

def leerProductos(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, "producto/lista.html", context)

def eliminarProducto(request, producto_modelo):
    producto = get_object_or_404(Producto, modelo=producto_modelo)
    if producto:
        producto.delete()
    productos_actualizados = Producto.objects.all()
    contexto = {"productos": productos_actualizados}
    return render(request, "producto/lista.html", contexto)

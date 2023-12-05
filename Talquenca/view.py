from django.shortcuts import render
from Users.forms import UsuarioFormulario, ProductoFormulario, ExperienciaFormulario
from Users.models import Usuario, Producto, Experiencia

#vistas
def index(request):
    return render(request, 'index.html')

def vista_de_formulario_usuario(request):
    if request.method == 'POST':
        nuevo_formulario = UsuarioFormulario(request.POST)

        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nuevo_usuario = Usuario(
                    nombre=informacion['nombre'], 
                    apellido=informacion['apellido'], 
                    email=informacion['email'])
            nuevo_usuario.save()
            return render(request, 'creado.html')
    else:
        nuevo_formulario  = UsuarioFormulario()
        return render(request, 'usuario.html', {'formulario': nuevo_formulario})


def vista_de_formulario_producto(request):
    if request.method == 'POST':
        nuevo_formulario = ProductoFormulario(request.POST)

        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data

            nuevo_producto = Producto(
                    modelo=informacion['modelo'], 
                    descripcion=informacion['descripcion'],
                    fecha_salida=informacion['fecha_salida']) 
            nuevo_producto.save()

            return render(request, 'creado.html')
    else:
        nuevo_formulario  = ProductoFormulario()
        return render(request, 'producto.html', {'formulario': nuevo_formulario})


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
        return render(request, 'experiencia.html', {'formulario': nuevo_formulario})





# def cursos_formukkklario(request):
#     if request.method == 'POST':
#         curso = Curso(resuest.post("curso"), request.post("camada"))
#         curso.save()
#         return render(request, 'index.html')
"""
URL configuration for Talquenca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from Talquenca.view import *
from Users.forms import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('producto/', vista_de_formulario_producto , name='producto'),
    path('experiencia/', vista_de_formulario_experiencia , name='experiencia'),

    #url de produtos 
    path('productos/', leerProductos , name='lista'),
    path('eliminarProducto/<producto_modelo>/', eliminarProducto , name='eliminarProducto'),
    path('editarProducto/<producto_modelo>/', editarProducto , name='eliminarProducto'),

    #url de usuarios
    path('login/', vista_de_login , name='login'),
    path('login/editar/', vista_de_edicion , name='editar_usuario'),

    path('registrarse/', vista_de_registro , name='registro'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html') ,name='logout'),
    path('login/editar/password', CambiarContrasenia.as_view(template_name='usuarios/constasena.html') ,name='editar_contrasenia'),

 ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

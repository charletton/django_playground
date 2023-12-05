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
from Talquenca.view import *
from Users.forms import UsuarioFormulario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('usuario/', vista_de_formulario_usuario , name='usuario'),
    path('producto/', vista_de_formulario_producto , name='producto'),
    path('experiencia/', vista_de_formulario_experiencia , name='experiencia'),
]

from django.contrib import admin

# Register your models here.

from Users.models import *

admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Experiencia)

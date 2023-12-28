from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=4)
    descripcion = models.TextField(default='Describir producto')
    imagenProducto = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return f'Producto: {self.modelo} - Autor: {self.autor.username}'

class Experiencia(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    mensaje = models.TextField(default='Escribe tu mensaje')
    puntaje = models.IntegerField(default=1)


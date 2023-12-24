from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.db import models

class Producto(models.Model):
    modelo = models.CharField(max_length=4)
    descripcion = models.CharField(max_length=20, default='Describir producto')
    imagenProducto = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return f'Producto: {self.modelo}'

class Experiencia(models.Model):
    mensaje = models.TextField(default = 'Escribe tu mensaje')
    puntaje = models.IntegerField(default=1,
        validators=[
            MinValueValidator(1, message="El valor debe ser 1 o mayor."),
            MaxValueValidator(10, message="El valor debe ser 10 o menor.")
        ]
    )




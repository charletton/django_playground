from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    email = models.EmailField()

    def __str__(self):
        return f'Cliente: {self.nombre}'


class Producto(models.Model):
    modelo = models.CharField(max_length = 4, default=1970)
    descripcion = models.CharField(max_length = 20, default = 'Describir producto')
    fecha_salida = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return f'Producto: {self.nombre}'

class Experiencia(models.Model):
    mensaje = models.TextField(default = 'Escribe tu mensaje')
    puntaje = models.IntegerField(default=1,
        validators=[
            MinValueValidator(1, message="El valor debe ser 1 o mayor."),
            MaxValueValidator(10, message="El valor debe ser 10 o menor.")
        ]
    )

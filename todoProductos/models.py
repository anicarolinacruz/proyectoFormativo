from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio =  models.PositiveIntegerField(
        verbose_name='Precio (COP)',
        validators=[MinValueValidator(0), MaxValueValidator(99999999)]
    )
    imagen = models.ImageField(verbose_name = "Imagen", upload_to='productos')

    def __str__(self):
        return self.nombre

from django.db import models
from django.core.validators import MinValueValidator

class Prenda(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    talla = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    
   
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    
    
    stock = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )
    
    marca = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
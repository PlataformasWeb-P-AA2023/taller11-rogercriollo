from django.db import models

# Create your models here.


class Edificio(models.Model):
    TIPO_CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=12, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    num_cuartos = models.PositiveIntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Departamento en {self.edificio.nombre} - Propietario: {self.propietario}"
    

        
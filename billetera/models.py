from django.db import models
from django.db import models
from django.contrib.auth.models import User



class Ingreso(models.Model):
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

class Gasto(models.Model):
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    es_fijo = models.BooleanField(default=False)

class Usuario(models.Model):
    porcentaje_ahorro = models.DecimalField(max_digits=5, decimal_places=2)

class Calculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ahorro = models.DecimalField(max_digits=10, decimal_places=2)
    ahorro_deseado = models.DecimalField(max_digits=10, decimal_places=2)
    ahorros_van_bien = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cálculo de {self.usuario.username}'
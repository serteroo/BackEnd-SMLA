from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self): return self.nombre


class Medicion(models.Model):
    fecha_hora = models.DateTimeField()
    consumo_wh = models.IntegerField()
    class Meta: ordering = ['-fecha_hora']
    def __str__(self): return f"{self.dispositivo} @ {self.fecha_hora} -> {self.consumo_wh} Wh"

class Alerta(models.Model):
    fecha_hora = models.DateTimeField()
    mensaje = models.CharField(max_length=200)
    limite_superado_wh = models.IntegerField()
    class Meta: ordering = ['-fecha_hora']
    def __str__(self): return f"⚠️ {self.dispositivo} @ {self.fecha_hora}"


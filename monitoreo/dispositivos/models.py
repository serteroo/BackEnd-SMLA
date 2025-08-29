from django.db import models

class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150, blank=True, null=True)
    class Meta: unique_together = ('nombre', 'ubicacion')
    def __str__(self): return f"{self.nombre} ({self.ubicacion})" if self.ubicacion else self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=120)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="dispositivos")
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT, related_name="dispositivos")
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    estado_activo = models.BooleanField(default=True)
    def __str__(self): return self.nombre




from django.contrib import admin
from .models import Categoria, Zona, Dispositivo, Medicion, Alerta

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display  = ("nombre", "categoria", "zona", "potencia_nominal_w", "estado_activo")
    list_filter   = ("categoria", "zona", "estado_activo")
    search_fields = ("nombre",)

admin.site.register(Categoria)
admin.site.register(Zona)
admin.site.register(Medicion)
admin.site.register(Alerta)
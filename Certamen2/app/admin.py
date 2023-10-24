from django.contrib import admin
from .models import Comunicado, Entidad
from django.core.exceptions import PermissionDenied
    
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "entidad", "visible", "autor")
    list_filter = ("fecha_publicacion",)

    def save_model(self, request, obj, form, change):
        if change and (str(obj.entidad) != str(request.user.groups.get())):
            raise PermissionDenied("No tienes permiso para editar este comunicado.")
        
        elif not change: 
            obj.autor = request.user
        else:
            obj.modificado_por = request.user
        super().save_model(request, obj, form, change)



admin.site.register(Entidad)
admin.site.register(Comunicado, ComunicadoAdmin)
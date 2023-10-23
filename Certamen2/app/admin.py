from django.contrib import admin
from .models import Comunicado, Entidad

# Register your models here.

admin.site.site_header = 'Administracion'


admin.site.register(Comunicado)
admin.site.register(Entidad)
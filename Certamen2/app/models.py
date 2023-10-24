from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entidad(models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/%Y/%m', verbose_name='Imagen')
    

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Entidades"
        


class Comunicado(models.Model):

    TIPO_CHOICES = [
        ('S', "Suspension de actividades"),
        ('C', "Suspension de clases"),
        ('I', "Informacion")
    ]
    titulo = models.CharField(max_length=50, unique=True)
    contenido = models.TextField()
    tipo = models.CharField(max_length=5, choices=TIPO_CHOICES, default='.')
    entidad = models.ForeignKey('Entidad', on_delete=models.CASCADE)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor', editable=False, null=True)
    modificado_por = models.ForeignKey(User, related_name="modificado_por", on_delete=models.CASCADE, editable=False, null=True)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Comunicado"
        verbose_name_plural = "Comunicados"
        ordering = ['id']
        
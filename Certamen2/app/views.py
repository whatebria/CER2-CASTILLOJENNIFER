from typing import Any
from django.shortcuts import render
from .models import Comunicado, Entidad


# Create your views here.

def Comunicados(request):
    title = 'Comunicados'
    departamento_selec = request.GET.get("departamento")

    if departamento_selec == 'all' or departamento_selec is None:
        comunicados = Comunicado.objects.all()
    else:
        departamento_filtrado = Entidad.objects.get(nombre=departamento_selec)
        comunicados = Comunicado.objects.filter(entidad=departamento_filtrado)


    data = {'title':title,
            'comunicados': comunicados.order_by('-fecha_publicacion'),
            'Departamentos':Entidad.objects.all(),
            'total_comunicados':comunicados.count(),
            'total_departamentos':Entidad.objects.count(),
            'departamento_selec':departamento_selec
            }

    return render(request, 'app/home.html', data)



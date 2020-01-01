# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Categoria,Nota
from app.services import Service
from app.functions import Function
from django.db.models import Count
import json

service = Service()
function = Function()

def agenda_estadisticas(request):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)

        textos_grafico = []
        series_grafico = []

        notas = Nota.objects.all()
        cantidad_notas = len(notas)
        categorias = Categoria.objects.annotate(cantidad=Count('nota'))

        for categoria in categorias:
            nombre_categoria = categoria.nombre
            cantidad = categoria.cantidad
            textos_grafico.append(nombre_categoria)
            data = {'name':nombre_categoria,'y':cantidad} 
            series_grafico.append(data)

        json_texto_grafico = json.dumps(textos_grafico)
        json_series_grafico = json.dumps(series_grafico)

        return render(request, 'estadisticas/index.html', {'usuario_logeado':usuario_logeado,'cantidad_notas':cantidad_notas,'textos_grafico':json_texto_grafico,'series_grafico':json_series_grafico})
    else:
        return redirect('agenda_ingreso')
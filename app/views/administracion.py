# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from app.services import Service
from app.functions import Function

service = Service()
function = Function()

def agenda_administracion(request):
    if service.validar_session(request):
        username = service.recibirUsuarioEnSesion(request)
        actividades = service.listarActividades("")
        fecha_actual = str(function.getFechaActual())
        lista_actividades = []
        for actividad in actividades:
            fecha = str(actividad.fecha)
            terminado = actividad.esta_terminado
            if fecha == fecha_actual and terminado == False:
                lista_actividades.append(actividad)
        return render(request, 'administracion/index.html', {'usuario_logeado':username,'actividades':lista_actividades})
    else:
        return redirect('agenda_ingreso')

def agenda_skin_sketchy(request):
    if service.validar_session(request):
        request.session['skin'] = 1
        return HttpResponse()
    else:
        return HttpResponse()

def agenda_skin_cursive(request):
    if service.validar_session(request):
        request.session['skin'] = 2
        return HttpResponse()
    else:
        return HttpResponse()
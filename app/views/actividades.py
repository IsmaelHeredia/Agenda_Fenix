# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib import messages
from app.models import Actividad
from app.services import Service
from app.functions import Function
from app.forms import ActividadForm
from django.core import serializers
from django.http import HttpResponse
import json
from datetime import datetime
from django.utils.dateformat import DateFormat

service = Service()
function = Function()

def agenda_actividad_list_json(request):
    if service.validar_session(request):  
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        actividades = Actividad.objects.all()
        fecha_actual = function.getFechaActualCalendario()
        json_pro = {}
        json_pro["fecha_actual"] = fecha_actual
        listas = []
        for actividad in actividades:
            id = actividad.id
            titulo = actividad.titulo
            fecha = str(actividad.fecha)
            hora = str(actividad.hora)
            fecha_hora = ""
            if not hora == "None":
                fecha_hora = fecha+"T"+hora
            else:
                fecha_hora = fecha
            url = reverse("agenda_actividad_read",args=(id,))
            color = ""
            if actividad.esta_terminado:
                color = "#3A87AD"
            else:
                color = "#F04124"
            listas.append({"title":titulo, "start":fecha_hora, "url":url, "backgroundColor":color, "borderColor":color})
        json_pro["actividades"] = listas
        json_lista = json.dumps(json_pro)
        return HttpResponse(json_lista, content_type='application/json')
    else:
        return redirect('agenda_ingreso')

def agenda_actividad_list(request):
    if service.validar_session(request):  
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        return render(request, 'actividades/actividad_list.html', {'usuario_logeado':usuario_logeado})
    else:
        return redirect('agenda_ingreso')

def agenda_actividad_view(request):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        if request.method == 'POST':
            form = ActividadForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                titulo = data['titulo']     
                fecha = data['fecha']        
                if service.comprobar_existencia_actividad_crear(titulo,fecha):
                    message_text = "La actividad %s ya existe" % (titulo,)
                    messages.add_message(request, messages.WARNING,message_text)
                    return redirect("agenda_actividad_view")
                else:
                    form.save()
                    message_text = "Actividad registrada"
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_actividad_list")
            else:
                message_text = "Faltan datos"
                messages.add_message(request, messages.WARNING,message_text)
                return redirect("agenda_actividad_view")
        else:
            return render(request, 'actividades/actividad_form.html', {'usuario_logeado':usuario_logeado,'form':ActividadForm(),'nuevo':True})
    else:
        return redirect('agenda_ingreso')

def agenda_actividad_read(request,id_actividad):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        actividad = get_object_or_404(Actividad, id=id_actividad)
        contenido = actividad.contenido
        contenido = function.proteger_cadena(contenido)
        contenido = function.generar_html(contenido)
        actividad.contenido = contenido
        return render(request,'actividades/actividad_read.html',{'usuario_logeado':usuario_logeado,'actividad':actividad})
    else:
        return redirect('agenda_ingreso')

def agenda_actividad_edit(request,id_actividad):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        actividad = get_object_or_404(Actividad, id=id_actividad)
        actividad.hora = function.convertirHora(actividad.hora)
        if request.method == 'GET':
            form = ActividadForm(instance=actividad)
        else:
            form = ActividadForm(request.POST,instance=actividad)
            if form.is_valid():
                data = form.cleaned_data
                titulo = data['titulo']
                fecha = data['fecha']
                if service.comprobar_existencia_actividad_editar(id_actividad,titulo,fecha):
                    message_text = "La actividad %s ya existe" % (titulo,)
                    messages.add_message(request, messages.WARNING,message_text)
                    return redirect("agenda_actividad_edit",id_actividad)
                else:
                    form.save()
                    message_text = "Actividad editada"
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_actividad_read",id_actividad)
            else:
                message_text = "Faltan datos"
                messages.add_message(request, messages.WARNING,message_text)  
                return redirect("agenda_actividad_edit",id_actividad)    
        return render(request,'actividades/actividad_form.html',{'usuario_logeado':usuario_logeado,'form':form,'actividad':actividad})
    else:
        return redirect('agenda_ingreso')

def agenda_actividad_delete(request,id_actividad):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        actividad = get_object_or_404(Actividad, id=id_actividad)
        if request.method == 'POST':
            if 'borrar_actividad' in request.POST:
                actividad.delete()
                message_text = "Actividad borrada"
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect('agenda_actividad_list')
            elif 'volver_lista' in request.POST:
                return redirect('agenda_actividad_list')    
        return render(request,'actividades/actividad_delete.html',{'usuario_logeado':usuario_logeado,'actividad':actividad})
    else:
        return redirect('agenda_ingreso')

def agenda_comprobar_fechas_activas(request):
    if service.validar_session(request):
        lista_actividades = []
        actividades_activas = []
        actividades = service.listarActividades("")
        fecha_actual = str(function.getFechaActual())
        hora_actual = str(function.getHoraActual())
        for actividad in actividades:
            id_actividad = actividad.id
            titulo = actividad.titulo
            fecha = str(actividad.fecha)
            hora = str(function.convertirHora(actividad.hora))
            terminado = actividad.esta_terminado
            if fecha == fecha_actual and hora == hora_actual and terminado == False:
                actividades_activas.append(actividad)
        lista_actividades = serializers.serialize('json', actividades_activas)
        return HttpResponse(lista_actividades)
    else:
        return HttpResponse()
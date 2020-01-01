# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Proyecto
from app.services import Service
from app.functions import Function
from app.forms import ProyectoForm
import json
from datetime import datetime
from django.utils.dateformat import DateFormat

service = Service()
function = Function()

def agenda_proyecto_list_json(request):
    if service.validar_session(request):
        proyectos = Proyecto.objects.all()
        cantidad = len(proyectos)
        json_pro = {}
        json_pro["draw"] = 1
        json_pro["recordsTotal"] = cantidad
        json_pro["recordsFiltered"] = cantidad
        listas = []
        for proyecto in proyectos:

            fecha_inicio_corta = ""
            fecha_inicio_normal = "Sin definir"
            fecha_terminado_corta = ""
            fecha_terminado_normal = "Sin definir"

            if proyecto.fecha_inicio:
                df1 = DateFormat(proyecto.fecha_inicio)
                fecha_inicio_corta = str(df1.format('Ymd'))
                fecha_inicio_normal = str(df1.format('d/m/Y'))

            if proyecto.fecha_terminado:
                df2 = DateFormat(proyecto.fecha_terminado)
                fecha_terminado_corta = str(df2.format('Ymd'))
                fecha_terminado_normal = str(df2.format('d/m/Y'))

            df3 = DateFormat(proyecto.fecha_registro)
            fecha_registro_corta = str(df3.format('YmdHi'))
            fecha_registro_normal = str(df3.format('d/m/Y H:i'))

            estado = proyecto.esta_terminado

            listas.append({"id":proyecto.id, "titulo":proyecto.titulo, "estado":estado, "fecha_inicio_normal":fecha_inicio_normal, "fecha_inicio_corta": fecha_inicio_corta, "fecha_terminado_normal":fecha_terminado_normal, "fecha_terminado_corta": fecha_terminado_corta, "fecha_registro_normal":fecha_registro_normal, "fecha_registro_corta": fecha_registro_corta})
        json_pro["data"] = listas
        json_lista = json.dumps(json_pro)
        return HttpResponse(json_lista, content_type='application/json')
    else:
        return redirect('agenda_ingreso')

def agenda_proyecto_list(request):
    if service.validar_session(request):  
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        return render(request, 'proyectos/proyecto_list.html', {'usuario_logeado':usuario_logeado})
    else:
        return redirect('agenda_ingreso')

def agenda_proyecto_view(request):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        if request.method == 'POST':
            form = ProyectoForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                titulo = data['titulo']     
                if service.comprobar_existencia_proyecto_crear(titulo):
                    message_text = "El proyecto %s ya existe" % (titulo,)
                    messages.add_message(request, messages.WARNING,message_text)
                    return redirect("agenda_proyecto_view")
                else:
                    form.save()
                    message_text = "Proyecto registrado"
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_proyecto_list")
            else:
                message_text = "Faltan datos"
                messages.add_message(request, messages.WARNING,message_text)
                return redirect("agenda_proyecto_view")
        else:
            return render(request, 'proyectos/proyecto_form.html', {'usuario_logeado':usuario_logeado,'form':ProyectoForm(),'nuevo':True})
    else:
        return redirect('agenda_ingreso')

def agenda_proyecto_read(request,id_proyecto):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        proyecto = get_object_or_404(Proyecto, id=id_proyecto)
        contenido = proyecto.contenido
        contenido = function.proteger_cadena(contenido)
        contenido = function.generar_html(contenido)
        proyecto.contenido = contenido
        return render(request,'proyectos/proyecto_read.html',{'usuario_logeado':usuario_logeado,'proyecto':proyecto})
    else:
        return redirect('agenda_ingreso')

def agenda_proyecto_edit(request,id_proyecto):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        proyecto = get_object_or_404(Proyecto, id=id_proyecto)
        if request.method == 'GET':
            form = ProyectoForm(instance=proyecto)
        else:
            form = ProyectoForm(request.POST,instance=proyecto)
            if form.is_valid():
                data = form.cleaned_data
                titulo = data['titulo']
                if service.comprobar_existencia_proyecto_editar(id_proyecto,titulo):
                    message_text = "El proyecto %s ya existe" % (titulo,)
                    messages.add_message(request, messages.WARNING,message_text)
                    return redirect("agenda_proyecto_edit",id_proyecto)
                else:
                    form.save()
                    message_text = "Proyecto editado"
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_proyecto_read",id_proyecto)
            else:
                message_text = "Faltan datos"
                messages.add_message(request, messages.WARNING,message_text)  
                return redirect("agenda_proyecto_edit",id_proyecto)    
        return render(request,'proyectos/proyecto_form.html',{'usuario_logeado':usuario_logeado,'form':form,'proyecto':proyecto})
    else:
        return redirect('agenda_ingreso')

def agenda_proyecto_delete(request,id_proyecto):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        proyecto = get_object_or_404(Proyecto, id=id_proyecto)
        if request.method == 'POST':
            if 'borrar_proyecto' in request.POST:
                proyecto.delete()
                message_text = "Proyecto borrado"
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect('agenda_proyecto_list')
            elif 'volver_lista' in request.POST:
                return redirect('agenda_proyecto_list')    
        return render(request,'proyectos/proyecto_delete.html',{'usuario_logeado':usuario_logeado,'proyecto':proyecto})
    else:
        return redirect('agenda_ingreso')
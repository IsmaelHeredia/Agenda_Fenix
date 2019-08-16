# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Proyecto
from app.services import Service
from app.functions import Function
from app.forms import ProyectoForm

service = Service()
function = Function()

def agenda_proyecto_list(request):
    if service.validar_session(request):  
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        proyectos = service.listarProyectos('')
        return render(request, 'proyectos/proyecto_list.html', {'usuario_logeado':usuario_logeado,'proyectos':proyectos})
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
                    message_text = function.mensaje("Proyectos","El proyecto "+titulo+" ya existe","warning")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_proyecto_view")
                else:
                    form.save()
                    message_text = function.mensaje("Proyectos","Proyecto registrado","success")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_proyecto_list")
            else:
                message_text = function.mensaje("Proyectos","Faltan datos","warning")
                messages.add_message(request, messages.SUCCESS,message_text)
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
                    message_text = function.mensaje("Proyectos","El proyecto "+titulo+" ya existe","warning")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_proyecto_edit",id_proyecto)
                else:
                    form.save()
                    message_text = function.mensaje("Proyectos","Proyecto editado","success")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_proyecto_read",id_proyecto)
            else:
                message_text = function.mensaje("Proyectos","Faltan datos","warning")
                messages.add_message(request, messages.SUCCESS,message_text)  
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
                message_text = function.mensaje("Proyectos","Proyecto borrado","success")
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect('agenda_proyecto_list')
            elif 'volver_lista' in request.POST:
                return redirect('agenda_proyecto_list')    
        return render(request,'proyectos/proyecto_delete.html',{'usuario_logeado':usuario_logeado,'proyecto':proyecto})
    else:
        return redirect('agenda_ingreso')
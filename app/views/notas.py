# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Nota
from app.services import Service
from app.functions import Function
from app.forms import NotaForm
from django.core import serializers
from django.http import HttpResponse
import json
from datetime import datetime
from django.utils.dateformat import DateFormat

service = Service()
function = Function()

def agenda_nota_list_json(request):
    if service.validar_session(request):
        notas = Nota.objects.all()
        cantidad = len(notas)
        json_pro = {}
        json_pro["draw"] = 1
        json_pro["recordsTotal"] = cantidad
        json_pro["recordsFiltered"] = cantidad
        listas = []
        for nota in notas:
            df = DateFormat(nota.fecha_registro)
            fecha_registro_corta = str(df.format('YmdHi'))
            fecha_registro_normal = str(df.format('d/m/Y H:i'))
            listas.append({"id":nota.id, "titulo":nota.titulo, "categoria":nota.categoria.nombre, "fecha_registro_normal":fecha_registro_normal, "fecha_registro_corta": fecha_registro_corta})
        json_pro["data"] = listas
        json_lista = json.dumps(json_pro)
        return HttpResponse(json_lista, content_type='application/json')
    else:
        return redirect('agenda_ingreso')

def agenda_nota_list(request):
    if service.validar_session(request):  
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        return render(request, 'notas/nota_list.html', {'usuario_logeado':usuario_logeado})
    else:
        return redirect('agenda_ingreso')

def agenda_nota_view(request):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        if request.method == 'POST':
            form = NotaForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                titulo = data['titulo']     
                categoria = data['categoria']           
                if service.comprobar_existencia_nota_crear(titulo,categoria):
                    message_text = "La nota %s ya existe" % (titulo,)
                    messages.add_message(request, messages.WARNING,message_text)
                    return redirect("agenda_nota_view")
                else:
                    form.save()
                    message_text = "Nota registrada"
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_nota_list")
            else:
                message_text = "Faltan datos"
                messages.add_message(request, messages.WARNING,message_text)
                return redirect("agenda_nota_view")
        else:
            return render(request, 'notas/nota_form.html', {'usuario_logeado':usuario_logeado,'form':NotaForm(),'nuevo':True})
    else:
        return redirect('agenda_ingreso')

def agenda_nota_read(request,id_nota):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        nota = get_object_or_404(Nota, id=id_nota)
        contenido = nota.contenido
        contenido = function.proteger_cadena(contenido)
        contenido = function.generar_html(contenido)
        nota.contenido = contenido
        return render(request,'notas/nota_read.html',{'usuario_logeado':usuario_logeado,'nota':nota})
    else:
        return redirect('agenda_ingreso')

def agenda_nota_edit(request,id_nota):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        nota = get_object_or_404(Nota, id=id_nota)
        if request.method == 'GET':
            form = NotaForm(instance=nota)
        else:
            form = NotaForm(request.POST,instance=nota)
            if form.is_valid():
                data = form.cleaned_data
                titulo = data['titulo']
                categoria = data['categoria']
                if service.comprobar_existencia_nota_editar(id_nota,titulo,categoria):
                    message_text = "La nota %s ya existe" % (titulo,)
                    messages.add_message(request, messages.WARNING,message_text)
                    return redirect("agenda_nota_edit",id_nota)
                else:
                    form.save()
                    message_text = "Nota editada"
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_nota_read",id_nota)                    
            else:
                message_text = "Faltan datos"
                messages.add_message(request, messages.WARNING,message_text)  
                return redirect("agenda_nota_edit",id_categoria)    
        return render(request,'notas/nota_form.html',{'usuario_logeado':usuario_logeado,'form':form,'nota':nota})
    else:
        return redirect('agenda_ingreso')

def agenda_nota_delete(request,id_nota):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        nota = get_object_or_404(Nota, id=id_nota)
        if request.method == 'POST':
            if 'borrar_nota' in request.POST:
                nota.delete()
                message_text = "Nota borrada"
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect('agenda_nota_list')
            elif 'volver_lista' in request.POST:
                return redirect('agenda_nota_list')    
        return render(request,'notas/nota_delete.html',{'usuario_logeado':usuario_logeado,'nota':nota})
    else:
        return redirect('agenda_ingreso')
# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Categoria
from app.services import Service
from app.functions import Function
from app.forms import CategoriaForm
import json
from datetime import datetime
from django.utils.dateformat import DateFormat

service = Service()
function = Function()

def agenda_categoria_list_json(request):
    if service.validar_session(request):
        categorias = Categoria.objects.all()
        cantidad = len(categorias)
        json_pro = {}
        json_pro["draw"] = 1
        json_pro["recordsTotal"] = cantidad
        json_pro["recordsFiltered"] = cantidad
        listas = []
        for categoria in categorias:
            listas.append({"id":categoria.id, "nombre":categoria.nombre})
        json_pro["data"] = listas
        json_lista = json.dumps(json_pro)
        return HttpResponse(json_lista, content_type='application/json')
    else:
        return redirect('agenda_ingreso')

def agenda_categoria_list(request):
    if service.validar_session(request):  
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        return render(request, 'categorias/categoria_list.html', {'usuario_logeado':usuario_logeado})
    else:
        return redirect('agenda_ingreso')

def agenda_categoria_view(request):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        if request.method == 'POST':
            form = CategoriaForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                nombre = data['nombre']                
                if service.comprobar_existencia_categoria_crear(nombre):
                    message_text = "La categoria %s ya existe" % (nombre,)
                    messages.add_message(request, messages.WARNING,message_text)
                    return redirect("agenda_categoria_view")
                else:
                    form.save()
                    message_text = "Categoria registrada"
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_categoria_list")
            else:
                message_text = "Faltan datos"
                messages.add_message(request, messages.WARNING,message_text)
                return redirect("agenda_categoria_view")
        else:
            return render(request, 'categorias/categoria_form.html', {'usuario_logeado':usuario_logeado,'form':CategoriaForm(),'nuevo':True})
    else:
        return redirect('agenda_ingreso')

def agenda_categoria_edit(request,id_categoria):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        categoria = get_object_or_404(Categoria, id=id_categoria)
        if request.method == 'GET':
            form = CategoriaForm(instance=categoria)
        else:
            form = CategoriaForm(request.POST,instance=categoria)
            if form.is_valid():
                data = form.cleaned_data
                nombre = data['nombre']
                if service.comprobar_existencia_categoria_editar(id_categoria,nombre):
                    message_text = "La categoria %s ya existe" % (nombre,)
                    messages.add_message(request, messages.WARNING,message_text)
                    return redirect("agenda_categoria_edit",id_proveedor)
                else:
                    form.save()
                    message_text = "Categoria editada"
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_categoria_list")                   
            else:
                message_text = "Faltan datos"
                messages.add_message(request, messages.WARNING,message_text)  
                return redirect("agenda_categoria_edit",id_categoria)    
        return render(request,'categorias/categoria_form.html',{'usuario_logeado':usuario_logeado,'form':form,'categoria':categoria})
    else:
        return redirect('agenda_ingreso')

def agenda_categoria_delete(request,id_categoria):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        categoria = get_object_or_404(Categoria, id=id_categoria)
        if request.method == 'POST':
            if 'borrar_categoria' in request.POST:
                categoria.delete()
                message_text = "Categoria borrada"
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect('agenda_categoria_list')
            elif 'volver_lista' in request.POST:
                return redirect('agenda_categoria_list')    
        return render(request,'categorias/categoria_delete.html',{'usuario_logeado':usuario_logeado,'categoria':categoria})
    else:
        return redirect('agenda_ingreso')
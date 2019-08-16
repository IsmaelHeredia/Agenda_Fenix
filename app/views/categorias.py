# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Categoria
from app.services import Service
from app.functions import Function
from app.forms import CategoriaForm

service = Service()
function = Function()

def agenda_categoria_list(request):
    if service.validar_session(request):  
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        categorias = service.listarCategorias('')
        return render(request, 'categorias/categoria_list.html', {'usuario_logeado':usuario_logeado,'categorias':categorias})
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
                    message_text = function.mensaje("Categorias","La categoria "+nombre+" ya existe","warning")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_categoria_view")
                else:
                    form.save()
                    message_text = function.mensaje("Categorias","Categoria registrada","success")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_categoria_list")
            else:
                message_text = function.mensaje("Categorias","Faltan datos","warning")
                messages.add_message(request, messages.SUCCESS,message_text)
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
                    message_text = function.mensaje("Categorias","La categoria "+nombre+" ya existe","warning")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_categoria_edit",id_proveedor)
                else:
                    form.save()
                    message_text = function.mensaje("Categorias","Categoria editada","success")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_categoria_list")                   
            else:
                message_text = function.mensaje("Categorias","Faltan datos","warning")
                messages.add_message(request, messages.SUCCESS,message_text)  
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
                message_text = function.mensaje("Categorias","Categoria borrada","success")
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect('agenda_categoria_list')
            elif 'volver_lista' in request.POST:
                return redirect('agenda_categoria_list')    
        return render(request,'categorias/categoria_delete.html',{'usuario_logeado':usuario_logeado,'categoria':categoria})
    else:
        return redirect('agenda_ingreso')
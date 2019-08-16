# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Nota
from app.services import Service
from app.functions import Function
from app.forms import NotaForm

service = Service()
function = Function()

def agenda_nota_list(request):
    if service.validar_session(request):  
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        notas = service.listarNotas('')
        return render(request, 'notas/nota_list.html', {'usuario_logeado':usuario_logeado,'notas':notas})
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
                    message_text = function.mensaje("Notas","La nota "+titulo+" ya existe","warning")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_nota_view")
                else:
                    form.save()
                    message_text = function.mensaje("Notas","Nota registrada","success")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_nota_list")
            else:
                message_text = function.mensaje("Notas","Faltan datos","warning")
                messages.add_message(request, messages.SUCCESS,message_text)
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
                    message_text = function.mensaje("Notas","La nota "+titulo+" ya existe","warning")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_nota_edit",id_nota)
                else:
                    form.save()
                    message_text = function.mensaje("Notas","Nota editada","success")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect("agenda_nota_read",id_nota)                    
            else:
                message_text = function.mensaje("Notas","Faltan datos","warning")
                messages.add_message(request, messages.SUCCESS,message_text)  
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
                message_text = function.mensaje("Notas","Nota borrada","success")
                messages.add_message(request, messages.SUCCESS,message_text)
                return redirect('agenda_nota_list')
            elif 'volver_lista' in request.POST:
                return redirect('agenda_nota_list')    
        return render(request,'notas/nota_delete.html',{'usuario_logeado':usuario_logeado,'nota':nota})
    else:
        return redirect('agenda_ingreso')
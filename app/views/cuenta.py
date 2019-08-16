# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Usuario,CambiarUsuario,CambiarClave
from app.services import Service
from app.functions import Function
from app.forms import CambiarUsuarioForm,CambiarClaveForm

service = Service()
function = Function()

def agenda_cambiar_usuario(request):
    if service.validar_session(request):
        if request.method == 'POST':
            form = CambiarUsuarioForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                nombre_usuario = data['usuario']
                nuevo_usuario = data['nuevo_usuario']
                clave = function.md5_encode(data['clave'])
                if service.ingreso_usuario(nombre_usuario,clave):
                    if service.comprobar_existencia_usuario_crear(nuevo_usuario):
                        message_text = function.mensaje("Usuarios","El usuario "+nombre_usuario+" ya existe","warning")
                        messages.add_message(request, messages.SUCCESS,message_text)
                        return redirect('agenda_cambiar_usuario')
                    else:
                        usuario = Usuario.objects.get(nombre=nombre_usuario)
                        usuario.nombre = nuevo_usuario
                        usuario.save()
                        del request.session['user_login']
                        message_text = function.mensaje("Cambiar Usuario","El usuario ha sido cambiado exitosamente, reinicie la aplicación","success")
                        messages.add_message(request, messages.SUCCESS,message_text)
                        return redirect('agenda_ingreso')
                else:
                    message_text = function.mensaje("Cambiar Usuario","Ingreso inválido","warning")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect('agenda_cambiar_usuario')

        else:
            usuario = service.recibirUsuarioEnSesion(request)
            form = CambiarUsuarioForm(initial={'usuario': usuario})
            return render(request, 'cuenta/cambiar_usuario.html', {'usuario_logeado':usuario,'form':form})
    else:
        return redirect('agenda_ingreso')

def agenda_cambiar_clave(request):
    if service.validar_session(request):
        if request.method == 'POST':
            form = CambiarClaveForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                nombre_usuario = data['usuario']
                clave = function.md5_encode(data['clave'])
                nueva_clave = function.md5_encode(data['nueva_clave'])
                if service.ingreso_usuario(nombre_usuario,clave):
                    usuario = Usuario.objects.get(nombre=nombre_usuario)
                    usuario.clave = nueva_clave
                    usuario.save()
                    del request.session['user_login']
                    message_text = function.mensaje("Cambiar Clave","La clave ha sido cambiada exitosamente, reinicie la aplicación","success")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect('agenda_ingreso')
                else:
                    message_text = function.mensaje("Cambiar Clave","Ingreso inválido","warning")
                    messages.add_message(request, messages.SUCCESS,message_text)
                    return redirect('agenda_cambiar_clave')

        else:
            usuario = service.recibirUsuarioEnSesion(request)
            form = CambiarClaveForm(initial={'usuario': usuario})
            return render(request, 'cuenta/cambiar_clave.html', {'usuario_logeado':usuario,'form':form})
    else:
        return redirect('agenda_ingreso')
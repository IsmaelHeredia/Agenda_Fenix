# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from app.services import Service
from app.functions import Function
from app.forms import IngresoForm

service = Service()
function = Function()

def agenda_ingreso(request):
    if not service.validar_instalacion():
        return redirect('agenda_instalar')
    else:
        if service.validar_session(request):
            return redirect('agenda_administracion')
        else:
            if request.method == 'POST':
                form = IngresoForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    username = data['usuario']
                    password = function.md5_encode(data['clave'])
                    if service.ingreso_usuario(username,password):
                        request.session['user_login'] = service.generarSesion(username,password)
                        return redirect('agenda_administracion')
                    else:
                        message_text = "Ingreso inválido"
                        messages.add_message(request, messages.WARNING,message_text)
                        return redirect('agenda_ingreso')
                else:
                    message_text = "Faltan datos"
                    messages.add_message(request, messages.WARNING,message_text)
            return render(request, 'ingreso/index.html', {'form':IngresoForm()})

def agenda_salir(request):
    if service.validar_session(request):
        del request.session['user_login']
        message_text = "La sesión ha sido cerrada"
        messages.add_message(request, messages.SUCCESS,message_text)
        return redirect('agenda_ingreso')
    else:
        return redirect('agenda_ingreso')
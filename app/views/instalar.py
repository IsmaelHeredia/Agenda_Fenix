# Written By Ismael Heredia in the year 2018

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from app.services import Service
from app.functions import Function
from app.forms import UsuarioForm

service = Service()
function = Function()

def agenda_instalar(request):
    if request.method == 'POST':
        request.POST._mutable = True
        form = UsuarioForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            obj = form.save(commit=False)
            password_encoded = function.md5_encode(obj.clave)
            obj.clave = password_encoded
            obj.save()
            message_text = function.mensaje("Instalación","Usuario registrado","success")
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect("agenda_ingreso")
        else:
            message_text = function.mensaje("Instalación","Datos inválidos","warning")
            messages.add_message(request, messages.SUCCESS,message_text)
            return redirect("agenda_instalar")            
    else:
        return render(request, 'instalar/index.html', {'form':UsuarioForm()})
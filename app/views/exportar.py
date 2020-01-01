# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from app.services import Service
from app.functions import Function
from app.forms import ExportarForm

service = Service()
function = Function()

def agenda_exportar(request):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        if request.method == 'POST':
            form = ExportarForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                directorio = data['directorio']
                if service.exportar_datos(directorio):
                    message_text = "Datos exportados"
                    messages.add_message(request, messages.SUCCESS,message_text)
                else:
                    message_text = "Ha ocurrido un error en la exportación"
                    messages.add_message(request, messages.ERROR,message_text)
                
                return render(request, 'exportar/index.html', {'usuario_logeado':usuario_logeado,'form':ExportarForm()})
        else:
            return render(request, 'exportar/index.html', {'usuario_logeado':usuario_logeado,'form':ExportarForm()})
    else:
        return redirect('agenda_ingreso')
# Written By Ismael Heredia in the year 2020

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
from app.services import Service
from app.functions import Function
from app.forms import ImportarForm

service = Service()
function = Function()

def agenda_importar(request):
    if service.validar_session(request):
        usuario_logeado = service.recibirUsuarioEnSesion(request)
        if request.method == 'POST':
            form = ImportarForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                directorio = data['directorio']
                message_text = ""
                if service.importar_datos(directorio):
                    message_text = "Datos importados"
                    messages.add_message(request, messages.SUCCESS,message_text)
                else:
                    message_text = "Ha ocurrido un error en la importación"
                    messages.add_message(request, messages.ERROR,message_text)
                
                return render(request, 'importar/index.html', {'usuario_logeado':usuario_logeado,'form':ImportarForm()})
        else:
            return render(request, 'importar/index.html', {'usuario_logeado':usuario_logeado,'form':ImportarForm()})
    else:
        return redirect('agenda_ingreso')
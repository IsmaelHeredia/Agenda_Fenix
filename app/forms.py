# Written By Ismael Heredia in the year 2020

from django import forms

from app.models import Ingreso,Usuario,Importar,Exportar,Categoria,Nota,Actividad,Proyecto,CambiarUsuario,CambiarClave

class IngresoForm(forms.ModelForm):
    
    class Meta:

        model = Ingreso
        
        fields=[
            'usuario',
            'clave',
        ]
        
        labels = {
            'usuario' : 'Usuario',
            'clave' : 'Clave',
        }

        widgets = {
            'usuario' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese usuario','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'clave' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese clave'}),    
        }

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        
        model = Usuario

        fields = [
            'nombre',
            'clave',
        ]

        labels = {
            'nombre':'Usuario',
            'clave':'Clave',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre de usuario','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'clave':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese clave'}),
        }

class ImportarForm(forms.ModelForm):
    
    class Meta:

        model = Importar
        
        fields=[
            'directorio',
        ]
        
        labels = {
            'directorio' : 'Directorio',
        }

        widgets = {
            'directorio' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese directorio','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
        }

class ExportarForm(forms.ModelForm):
    
    class Meta:

        model = Exportar
        
        fields=[
            'directorio',
        ]
        
        labels = {
            'directorio' : 'Directorio',
        }

        widgets = {
            'directorio' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese directorio','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
        }

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        
        model = Categoria

        fields = [
            'nombre',
        ]

        labels = {
            'nombre':'Nombre',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre de categoria','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
        }

        ordering = ['nombre']

class NotaForm(forms.ModelForm):

    class Meta:
        
        model = Nota

        fields = [
            'titulo',
            'contenido',
            'categoria',
        ]

        labels = {
            'titulo':'Título',
            'contenido':'Contenido',
            'categoria':'Categoria',
        }

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese título','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'contenido':forms.Textarea(attrs={'class':'form-control textarea-css','rows':15,'placeholder':'Ingrese contenido','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),        
        }

class ProyectoForm(forms.ModelForm):
    
    esta_terminado = forms.BooleanField(required=False, initial=False)

    class Meta:
        
        model = Proyecto

        fields = [
            'titulo',
            'contenido',
            'fecha_inicio',
            'fecha_terminado',
            'esta_terminado',
        ]

        labels = {
            'titulo':'Título',
            'contenido':'Contenido',
            'fecha_inicio':'Fecha inicio',
            'fecha_terminado':'Fecha terminado',
            'esta_terminado':'Estado'
        }

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese título','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'contenido':forms.Textarea(attrs={'class':'form-control textarea-css','rows':15,'placeholder':'Ingrese contenido','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'fecha_inicio':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese fecha inicio'}),
            'fecha_terminado':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese fecha terminado'}),
        }

class ActividadForm(forms.ModelForm):
    
    esta_terminado = forms.BooleanField(required=False, initial=False)

    class Meta:
        
        model = Actividad

        fields = [
            'titulo',
            'contenido',
            'fecha',
            'hora',
            'esta_terminado',
        ]

        labels = {
            'titulo':'Título',
            'contenido':'Contenido',
            'fecha':'Fecha',
            'hora':'Hora',
            'esta_terminado':'Estado'
        }

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese título','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'contenido':forms.Textarea(attrs={'class':'form-control textarea-css','rows':15,'placeholder':'Ingrese contenido','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'fecha':forms.TextInput(attrs={'class':'form-control','placeholder':'Seleccione fecha','data-date-format':'mm/dd/yyyy'}),
            'hora':forms.TextInput(attrs={'class':'form-control','placeholder':'Seleccione hora'}),
        }

class CambiarUsuarioForm(forms.ModelForm):
    
    class Meta:

        model = CambiarUsuario
        
        fields = [
            'usuario',
            'nuevo_usuario',
            'clave',
        ]

        labels = {
            'usuario':'Nombre usuario',
            'nuevo_usuario':'Nuevo usuario',
            'clave':'Clave',
        }

        widgets = {   
            'usuario':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre de usuario','readonly':'readonly'}),
            'nuevo_usuario':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nuevo nombre','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'clave':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese clave'}),       
        }

class CambiarClaveForm(forms.ModelForm):
    
    class Meta:

        model = CambiarClave
        
        fields = [
            'usuario',
            'clave',
            'nueva_clave',
        ]

        labels = {
            'usuario':'Nombre usuario',
            'clave':'Clave',
            'nueva_clave':'Nueva clave',
        }

        widgets = {   
            'usuario':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre de usuario','readonly':'readonly'}),
            'clave':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese clave'}),
            'nueva_clave':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese nueva clave'}),       
        }
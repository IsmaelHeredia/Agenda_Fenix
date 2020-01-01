# Written By Ismael Heredia in the year 2020

import os,time,datetime,re
from app.functions import Function
from app.models import Usuario,Categoria,Nota,Actividad,Proyecto

function = Function()

class Service(object):

    def ingreso_usuario(self,username,password):
        response = False
        function = Function()
        try:
            o = Usuario.objects.get(nombre=username, clave=password)
            response = True
        except Usuario.DoesNotExist:
            response = False
        return response

    def generarSesion(self,username,password):
        function = Function()
        contenido = function.base64_encode(username+":"+password)
        return contenido

    def recibirUsuarioEnSesion(self,request):
        function = Function()
        username = ""
        if 'user_login' in request.session:
            contenido = function.base64_decode(request.session['user_login'])
            datos = contenido.split(":")
            if datos:
                username = datos[0]
        return username

    def validar_instalacion(self):
        usuarios = Usuario.objects.all() 
        if usuarios:
            return True
        else:
            return False

    def validar_session(self,request):
        function = Function()
        response = False
        if 'user_login' in request.session:
            contenido = function.base64_decode(request.session['user_login'])
            datos = contenido.split(":")
            if datos:
                username = datos[0]
                password = datos[1]
                if self.ingreso_usuario(username,password):
                    response = True
                else:
                    response = False
        return response

    def listarUsuarios(self,patron):
        try:
            return Usuario.objects.filter(nombre_usuario__icontains=patron).order_by('id')
        except Exception as e:
            pass

    def listarCategorias(self,patron):
        try:
            return Categoria.objects.filter(nombre__icontains=patron).order_by('nombre')
        except Exception as e:
            pass

    def listarNotas(self,patron):
        try:
            return Nota.objects.filter(titulo__icontains=patron).order_by('id')
        except Exception as e:
            pass

    def listarNotasPorCategoria(self,categoria):
        try:
            return Nota.objects.filter(categoria=categoria).order_by('id')
        except Exception as e:
            pass

    def listarActividades(self,patron):
        try:
            return Actividad.objects.filter(titulo__icontains=patron).order_by('id')
        except Exception as e:
            pass 

    def listarProyectos(self,patron):
        try:
            return Proyecto.objects.filter(titulo__icontains=patron).order_by('id')
        except Exception as e:
            pass 

    def comprobar_existencia_categoria_crear(self,nombre):
        response = False
        try:
            o = Categoria.objects.get(nombre=nombre)
            response = True
        except Categoria.DoesNotExist:
            response = False
        return response

    def comprobar_existencia_categoria_editar(self,id,nombre):
        if Categoria.objects.filter(nombre=nombre).exclude(id=id).exists():
            return True
        else:
            return False

    def comprobar_existencia_nota_crear(self,titulo,categoria):
        response = False
        try:
            o = Nota.objects.get(titulo=titulo,categoria=categoria)
            response = True
        except Nota.DoesNotExist:
            response = False
        return response

    def comprobar_existencia_nota_editar(self,id,titulo,categoria):
        if Nota.objects.filter(titulo=titulo,categoria=categoria).exclude(id=id).exists():
            return True
        else:
            return False

    def comprobar_existencia_actividad_crear(self,titulo,fecha):
        response = False
        try:
            o = Actividad.objects.get(titulo=titulo,fecha=fecha)
            response = True
        except Actividad.DoesNotExist:
            response = False
        return response

    def comprobar_existencia_actividad_editar(self,id,titulo,fecha):
        if Actividad.objects.filter(titulo=titulo,fecha=fecha).exclude(id=id).exists():
            return True
        else:
            return False

    def comprobar_existencia_proyecto_crear(self,titulo):
        response = False
        try:
            o = Proyecto.objects.get(titulo=titulo)
            response = True
        except Proyecto.DoesNotExist:
            response = False
        return response

    def comprobar_existencia_proyecto_editar(self,id,titulo):
        if Proyecto.objects.filter(titulo=titulo).exclude(id=id).exists():
            return True
        else:
            return False

    def comprobar_existencia_usuario_crear(self,usuario):
        response = False
        try:
            o = Usuario.objects.get(nombre=usuario)
            response = True
        except Usuario.DoesNotExist:
            response = False
        return response

    def importar_datos(self,directorio):

        respuesta = False

        try:
            if os.path.exists(directorio):
                
                print("Importando datos ...\n")

                directorio_notas = directorio + "\\Notas"
                directorio_proyectos = directorio + "\\Proyectos"
                directorio_actividades = directorio + "\\Actividades"

                print("\nListando categorias ...\n")

                if os.path.isdir(directorio_notas):
                    categorias = os.listdir(directorio_notas)

                    for categoria in categorias:
                        categoria_ruta = directorio_notas + "/" + categoria
                        if os.path.isdir(categoria_ruta):
                            print("\nCategoria : "+categoria)

                            categoria_object = Categoria()
                            categoria_object.nombre = categoria
                            categoria_object.save()

                            categoria_nota = Categoria.objects.get(nombre=categoria)

                            notas = os.listdir(categoria_ruta)
                            for nota in notas:
                                nota_ruta = directorio_notas + "/" + categoria + "/" + nota
                                if os.path.isfile(nota_ruta):
                                    nombre = os.path.splitext(nota)[0]
                                    fecha_registro = function.recibirFechaRegistro(nota_ruta)
                                    print("Nota : "+nombre)
                                    print("Fecha registro : "+str(fecha_registro))
                                    contenido = function.leer_archivo(nota_ruta)

                                    nota_object = Nota()
                                    nota_object.titulo = nombre
                                    nota_object.contenido = contenido
                                    nota_object.categoria = categoria_nota
                                    nota_object.fecha_registro = fecha_registro
                                    nota_object.save()

                else:
                    print("No se encontraron categorias")

                print("\nListando actividades ...\n")

                if os.path.isdir(directorio_actividades):
                    actividades = os.listdir(directorio_actividades)

                    for actividad in actividades:
                        actividad_ruta = directorio_actividades + "/" + actividad
                        if os.path.isfile(actividad_ruta):
                            nombre = os.path.splitext(actividad)[0]
                            print("actividad : "+nombre)
                            contenido = function.leer_archivo(actividad_ruta)

                            fecha = None
                            hora = None
                            esta_terminado = False

                            regex = re.findall(r"\[\+\] Fecha : (.*)", contenido)
                            if regex:
                                fecha =  regex[0]

                            regex = re.findall(r"\[\+\] Hora : (.*)", contenido)
                            if regex:
                                hora =  regex[0]
                        
                            regex = re.findall(r"\[\+\] Terminado : (.*)", contenido)
                            if regex:
                                if regex[0] == "1":
                                    esta_terminado = True

                            contenido = function.cortar_archivo(actividad_ruta,4)

                            print("Fecha : "+str(fecha))
                            print("Hora : "+str(hora))
                            print("Terminado : "+str(esta_terminado))

                            actividad_object = Actividad()
                            actividad_object.titulo = nombre
                            actividad_object.contenido = contenido
                            actividad_object.esta_terminado = esta_terminado
                            actividad_object.fecha = fecha
                            actividad_object.hora = hora
                            actividad_object.save()
                else:
                    print("No se encontraron actividades")

                print("\nListando proyectos ...\n")

                if os.path.isdir(directorio_proyectos):
                    proyectos = os.listdir(directorio_proyectos)

                    for proyecto in proyectos:
                        proyecto_ruta = directorio_proyectos + "/" + proyecto
                        if os.path.isfile(proyecto_ruta):
                            nombre = os.path.splitext(proyecto)[0]
                            fecha_registro = function.recibirFechaRegistro(proyecto_ruta)

                            print("\n##################################\n")

                            print("Proyecto : "+nombre)
                            print("Fecha registro : "+fecha_registro)
                            contenido = function.leer_archivo(proyecto_ruta)
        
                            fecha_inicio = None
                            fecha_terminado = None
                            esta_terminado = False

                            regex = re.findall(r"\[\+\] Fecha inicio : (.*)", contenido)
                            if regex:
                                fecha_inicio =  regex[0]

                            regex = re.findall(r"\[\+\] Fecha terminado : (.*)", contenido)
                            if regex:
                                fecha_terminado =  regex[0]

                            regex = re.findall(r"\[\+\] Terminado : (.*)", contenido)
                            if regex:
                                if regex[0] == "1":
                                    esta_terminado = True

                            contenido = function.cortar_archivo(proyecto_ruta,4)

                            print("Fecha inicio : " + str(fecha_inicio))
                            print("Fecha terminado : " + str(fecha_terminado))
                            print("Terminado : " + str(esta_terminado))

                            proyecto_object = Proyecto()
                            proyecto_object.titulo = nombre
                            proyecto_object.contenido = contenido
                            proyecto_object.fecha_registro = fecha_registro
                            proyecto_object.fecha_inicio = fecha_inicio
                            proyecto_object.fecha_terminado = fecha_terminado
                            proyecto_object.esta_terminado = esta_terminado
                            proyecto_object.save()

                            print("\n##################################\n")
                else:
                    print("No se encontraron proyectos")

                respuesta = True

        except:
            raise

        return respuesta

    def exportar_datos(self,directorio):

        respuesta = False

        try:
            if os.path.exists(directorio):   

                directorio_notas = directorio + "\\" + "Notas"

                categorias = self.listarCategorias("")
                for categoria in categorias:
                    categoria_nombre = categoria.nombre
                    directorio_categoria = directorio_notas + "\\" + categoria_nombre
                    if not os.path.exists(directorio_categoria):
                        os.makedirs(directorio_categoria)
                        print("Directorio : "+directorio_categoria)
                        notas = self.listarNotasPorCategoria(categoria)
                        for nota in notas:
                            nota_titulo = nota.titulo
                            nota_contenido = nota.contenido
                            nota_archivo = nota_titulo + ".txt"
                            nota_fecha_registro = nota.fecha_registro
                            nota_directorio = directorio_categoria + "\\" + nota_archivo
                            if not os.path.isfile(nota_directorio):
                                function.crear_archivo(nota_directorio,nota_contenido)
                                function.cambiar_fecha(nota_directorio,nota_fecha_registro)
                                print("Nota : "+nota_directorio)
                                print("Fecha : "+str(nota_fecha_registro))

                directorio_actividades = directorio + "\\" + "Actividades"

                if not os.path.exists(directorio_actividades):
                    os.makedirs(directorio_actividades)
                    actividades = self.listarActividades("")
                    for actividad in actividades:
                        actividad_titulo = actividad.titulo
                        actividad_contenido = actividad.contenido
                        actividad_fecha = str(actividad.fecha)
                        actividad_hora = str(actividad.hora) 
                        actividad_esta_terminado = 0

                        if actividad.esta_terminado:
                            actividad_esta_terminado = 1

                        if actividad_fecha == "None":
                            actividad_fecha = ""

                        if actividad_hora == "None":
                            actividad_hora = ""

                        actividad_archivo = actividad_titulo + ".txt"
                        actividad_directorio = directorio_actividades + "\\" + actividad_archivo
                        if not os.path.isfile(actividad_directorio):
                            datos_fecha = ""
                            if actividad_fecha == "":
                                datos_fecha = "[+] Fecha :"
                            else:
                                datos_fecha = "[+] Fecha : " + actividad_fecha
                            datos_hora = ""
                            if actividad_hora == "":
                                datos_hora = "[+] Hora :"
                            else:
                                datos_hora = "[+] Hora : " + actividad_hora
                            datos_esta_terminado = "[+] Terminado : " + str(actividad_esta_terminado)
                            datos_actividad = datos_fecha + "\n" + datos_hora + "\n" + datos_esta_terminado
                            actividad_contenido = datos_actividad + "\n\n" + actividad_contenido
                            function.crear_archivo(actividad_directorio,actividad_contenido)
                            print("Actividad : "+actividad_directorio)

                directorio_proyectos = directorio + "\\" + "Proyectos"

                if not os.path.exists(directorio_proyectos):
                    os.makedirs(directorio_proyectos)
                    proyectos = self.listarProyectos("")
                    for proyecto in proyectos:
                        proyecto_titulo = proyecto.titulo
                        proyecto_contenido = proyecto.contenido
                        proyecto_fecha_inicio = str(proyecto.fecha_inicio)
                        proyecto_fecha_terminado = str(proyecto.fecha_terminado)
                        proyecto_esta_terminado = 0

                        if proyecto.esta_terminado:
                            proyecto_esta_terminado = 1

                        if proyecto_fecha_inicio == "None":
                            proyecto_fecha_inicio = ""

                        if proyecto_fecha_terminado == "None":
                            proyecto_fecha_terminado = ""

                        proyecto_fecha_registro = proyecto.fecha_registro
                        proyecto_archivo = proyecto_titulo + ".txt"
                        proyecto_directorio = directorio_proyectos + "\\" + proyecto_archivo
                        if not os.path.isfile(proyecto_directorio):
                            datos_fecha_inicio = ""
                            if proyecto_fecha_inicio == "":
                                datos_fecha_inicio = "[+] Fecha inicio :"
                            else:
                                 datos_fecha_inicio = "[+] Fecha inicio : " + proyecto_fecha_inicio   
                            datos_fecha_terminado = ""
                            if proyecto_fecha_terminado == "":                            
                                datos_fecha_terminado = "[+] Fecha terminado :"
                            else:
                                datos_fecha_terminado = "[+] Fecha terminado : " + proyecto_fecha_terminado
                            datos_esta_terminado = "[+] Terminado : " + str(proyecto_esta_terminado)
                            datos_proyecto = datos_fecha_inicio + "\n" + datos_fecha_terminado + "\n" + datos_esta_terminado
                            proyecto_contenido = datos_proyecto + "\n\n" + proyecto_contenido
                            function.crear_archivo(proyecto_directorio,proyecto_contenido)
                            function.cambiar_fecha(proyecto_directorio,proyecto_fecha_registro)
                            print("Proyecto : "+proyecto_directorio)

                print("Datos exportados")

                respuesta = True

        except:
            raise

        return respuesta

    def destroy(self):
        pass
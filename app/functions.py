# Written By Ismael Heredia in the year 2018

import base64,hashlib,os,sys,time,datetime,time,re
from time import gmtime, strftime
#import pywintypes, win32file, win32con
from django.utils.html import escape
from django.utils.safestring import mark_safe

class Function(object):

    #locale.setlocale(locale.LC_ALL, "es-AR")

    def mensaje(self,titulo,contenido,tipo):
        return "<script>"+ \
        "swal({"+ \
                "title: '"+titulo+"',"+ \
                "text: '"+contenido+"',"+ \
                "type:'"+tipo+"',"+ \
                "html:true,"+ \
                "animation: false,"+ \
                "confirmButtonText: 'Aceptar'"+ \
         "});"+ \
        "</script>"

    def mensaje_con_redireccion(self,titulo,contenido,tipo,ruta):
        return "<script>"+ \
        "swal({"+ \
                "title: '"+titulo+"',"+ \
                "text: '"+contenido+"',"+ \
                "type:'"+tipo+"',"+ \
                "html:true,"+ \
                "animation: false,"+ \
                "confirmButtonText: 'Aceptar'"+ \
         "},function() {"+ \
            "window.location.href = '"+ruta+"';"+ \
         "});"+ \
        "</script>"

    def getFecha(self):
        return time.strftime("%Y-%m-%d %H:%M:%S")

    def getFechaActual(self):
        return time.strftime("%Y-%m-%d")

    def getHoraActual(self):
        return time.strftime("%H:%M")

    def getFechaActualCalendario(self):
        return time.strftime("%Y-%m-%d")

    def convertirHora(self,hora):
        hora = str(hora)
        regex = re.findall(r"(.*):(.*):(.*)",hora)
        hora_parseada = ""
        if regex:
            matches = regex[0]
            hora = matches[0]
            minuto = matches[1]
            segundos = matches[2]
            hora_parseada = hora + ":" + minuto
        return hora_parseada

    def valid_digit(self,text):
        return text.isdigit()

    def md5_encode(self,text):
        encode = hashlib.md5()
        encode.update(text.encode("utf-8"))
        return encode.hexdigest()

    def base64_encode(self,text):
        encoded = base64.b64encode(text.encode())
        return encoded.decode('utf-8')

    def base64_decode(self,text):
        decoded = base64.b64decode(text.encode())
        return decoded.decode('utf-8')

    def leer_archivo(self,archivo):
        file = open(archivo, "r", encoding = "ISO-8859-1") 
        return file.read()

    def leer_lineas_archivo(self,archivo):
        file = open(archivo, "r", encoding = "ISO-8859-1") 
        return file.read().splitlines()

    def cortar_archivo(self,archivo,limite):
        lineas = self.leer_lineas_archivo(archivo)
        for i in range(0,limite):
            del lineas[0]
        contenido = ""
        for linea in lineas:
            contenido = contenido + linea + "\n"
        contenido = contenido[:-1]
        return contenido

    def recibirFechaRegistro(self,archivo):
        fecha_extraida = os.path.getctime(archivo)
        fecha_registro = datetime.datetime.fromtimestamp(fecha_extraida)
        return fecha_registro.strftime('%Y-%m-%d %H:%M:%S')

    def limpiarFecha(self,fecha):
        date = datetime.datetime.strptime(str(fecha), '%Y-%m-%d').date()
        return date.strftime('%d/%m/%Y')

    def crear_archivo(self,archivo,texto):
        with open(archivo,'w',encoding = "ISO-8859-1") as f:
            f.write(texto)

    def convertir_a_datetime(self,fecha):
        datetime_object = datetime.datetime.strptime(str(fecha), '%Y-%m-%d %H:%M:%S')
        return datetime_object

    def cambiar_fecha(self,archivo, datetime):
        datetime = self.convertir_a_datetime(datetime)
        datetime_ready = time.mktime(datetime.timetuple())
        wintime = pywintypes.Time(datetime_ready)
        winfile = win32file.CreateFile(
            archivo, win32con.GENERIC_WRITE,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None, win32con.OPEN_EXISTING,
            win32con.FILE_ATTRIBUTE_NORMAL, None)

        win32file.SetFileTime(winfile, wintime, None, None)

        winfile.close()

    def generar_html(self,contenido):

        resultado = ""

        lineas = contenido.split("\n")

        for linea in lineas:
            regex = re.findall(r"\[url\=(.*)\](.*)\[/url\]", linea)
            if regex:
                matches = regex[0]
                link = matches[0]
                nombre = matches[1]
                url = "[url=" + link + "]" + nombre + "[/url]"
                linea = linea.replace(url,"<a href='" + link + "'>" + nombre + "</a>")
            regex = re.findall(r"\[url\](.*)\[/url\]", linea)
            if regex:
                link = regex[0]
                url = "[url]" + link + "[/url]"
                linea = linea.replace(url,"<a href='" + link + "'>" + link + "</a>")

            linea = linea.replace("[center]","<center>")
            linea = linea.replace("[/center]","</center>")

            linea = linea.replace("[b]","<b>")
            linea = linea.replace("[/b]","</b>")

            linea = linea.replace("[img]","<img src='")
            linea = linea.replace("[/img]","'>")

            linea = linea.replace("[video]","<iframe width='800' height='500' src='")
            linea = linea.replace("[/video]","'></iframe>")

            linea = linea.replace("[lista]","<ul class='list-group'>")
            linea = linea.replace("[/lista]","</ul>")

            linea = linea.replace("[titulo]","<li class='list-group-item'><b>")
            linea = linea.replace("[/titulo]","</b></li>")

            linea = linea.replace("[item]","<li class='list-group-item'>")
            linea = linea.replace("[/item]","</li>")

            linea = linea.replace("[estado=completo]","<i class='fa fa-check-square nbsp' aria-hidden='true'></i>")

            linea = linea.replace("[estado=incompleto]","<i class='fa fa-minus-square nbsp' aria-hidden='true'></i>")

            linea = linea.replace("[estado=enproceso]","<i class='fa fa-question-circle-o' aria-hidden='true'></i>")

            resultado = resultado + linea + "\n"

        return resultado

    def proteger_cadena(self,contenido):
        contenido = contenido.replace("&","&amp;")
        contenido = contenido.replace("<","&lt;")
        contenido = contenido.replace(">","&gt;")
        return contenido

    def destroy(self):
        pass
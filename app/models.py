# Written By Ismael Heredia in the year 2020

from django.db import models
import datetime

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    clave = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria)
    fecha_registro = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.fecha_registro is None:
            self.fecha_registro = datetime.datetime.now()
        super(Nota, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Actividad(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    esta_terminado = models.BooleanField()
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Proyecto(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha_registro = models.DateTimeField()
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_terminado = models.DateField(null=True, blank=True)
    esta_terminado = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.fecha_registro is None:
            self.fecha_registro = datetime.datetime.now()
        super(Proyecto, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Ingreso(models.Model):
    usuario = models.CharField(max_length=150)
    clave = models.CharField(max_length=150)

    class Meta:
        managed = False

    def __str__(self):
        return self.usuario

class Buscador(models.Model):
    nombre_buscar = models.CharField(max_length=150)

    class Meta:
        managed = False

    def __str__(self):
        return self.nombre_buscar

class CambiarUsuario(models.Model):
    usuario = models.CharField(max_length=150)
    nuevo_usuario = models.CharField(max_length=150)
    clave = models.CharField(max_length=150)

    class Meta:
        managed = False

    def __str__(self):
        return self.usuario

class CambiarClave(models.Model):
    usuario = models.CharField(max_length=150)
    clave = models.CharField(max_length=150)
    nueva_clave = models.CharField(max_length=150)

    class Meta:
        managed = False

    def __str__(self):
        return self.usuario

class Importar(models.Model):
    directorio = models.CharField(max_length=300)

    class Meta:
        managed = False

    def __str__(self):
        return self.directorio

class Exportar(models.Model):
    directorio = models.CharField(max_length=300)

    class Meta:
        managed = False

    def __str__(self):
        return self.directorio
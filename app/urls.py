# Written By Ismael Heredia in the year 2020

from django.conf.urls import include, url
from app.views import instalar,ingreso,administracion,importar,exportar,categorias,notas,actividades,proyectos,estadisticas,cuenta

urlpatterns = [

    url(r'^$', ingreso.agenda_ingreso, name='agenda_inicio'),
    url(r'^instalar/$', instalar.agenda_instalar, name='agenda_instalar'),

    url(r'^ingreso/$',  ingreso.agenda_ingreso, name='agenda_ingreso'),
    url(r'^administracion/salir/$',  ingreso.agenda_salir, name='agenda_salir'),

    url(r'^administracion/$',  administracion.agenda_administracion, name='agenda_administracion'),

    url(r'^administracion/skins/sketchy/$',  administracion.agenda_skin_sketchy, name='agenda_skin_sketchy'),
    url(r'^administracion/skins/cursive/$',  administracion.agenda_skin_cursive, name='agenda_skin_cursive'),

    url(r'^administracion/categorias/cargarJson$', categorias.agenda_categoria_list_json, name='agenda_categoria_list_json'),
    url(r'^administracion/categorias/$',  categorias.agenda_categoria_list, name='agenda_categoria_list'),
    url(r'^administracion/categorias/agregar$', categorias.agenda_categoria_view, name='agenda_categoria_view'),
    url(r'^administracion/categorias/editar/(?P<id_categoria>\d+)/$', categorias.agenda_categoria_edit, name='agenda_categoria_edit'),
    url(r'^administracion/categorias/borrar/(?P<id_categoria>\d+)/$', categorias.agenda_categoria_delete, name='agenda_categoria_delete'),

    url(r'^administracion/notas/cargarJson$', notas.agenda_nota_list_json, name='agenda_nota_list_json'),
    url(r'^administracion/notas/$',  notas.agenda_nota_list, name='agenda_nota_list'),
    url(r'^administracion/notas/agregar$', notas.agenda_nota_view, name='agenda_nota_view'),
    url(r'^administracion/notas/leer/(?P<id_nota>\d+)/$', notas.agenda_nota_read, name='agenda_nota_read'),
    url(r'^administracion/notas/editar/(?P<id_nota>\d+)/$', notas.agenda_nota_edit, name='agenda_nota_edit'),
    url(r'^administracion/notas/borrar/(?P<id_nota>\d+)/$', notas.agenda_nota_delete, name='agenda_nota_delete'),

    url(r'^administracion/actividades/cargarJson$', actividades.agenda_actividad_list_json, name='agenda_actividad_list_json'),
    url(r'^administracion/actividades/$',  actividades.agenda_actividad_list, name='agenda_actividad_list'),
    url(r'^administracion/actividades/agregar$', actividades.agenda_actividad_view, name='agenda_actividad_view'),
    url(r'^administracion/actividades/leer/(?P<id_actividad>\d+)/$', actividades.agenda_actividad_read, name='agenda_actividad_read'),
    url(r'^administracion/actividades/editar/(?P<id_actividad>\d+)/$', actividades.agenda_actividad_edit, name='agenda_actividad_edit'),
    url(r'^administracion/actividades/borrar/(?P<id_actividad>\d+)/$', actividades.agenda_actividad_delete, name='agenda_actividad_delete'),
    
    url(r'^administracion/proyectos/cargarJson$', proyectos.agenda_proyecto_list_json, name='agenda_proyecto_list_json'),
    url(r'^administracion/proyectos/$',  proyectos.agenda_proyecto_list, name='agenda_proyecto_list'),
    url(r'^administracion/proyectos/agregar$', proyectos.agenda_proyecto_view, name='agenda_proyecto_view'),
    url(r'^administracion/proyectos/leer/(?P<id_proyecto>\d+)/$', proyectos.agenda_proyecto_read, name='agenda_proyecto_read'),
    url(r'^administracion/proyectos/editar/(?P<id_proyecto>\d+)/$', proyectos.agenda_proyecto_edit, name='agenda_proyecto_edit'),
    url(r'^administracion/proyectos/borrar/(?P<id_proyecto>\d+)/$', proyectos.agenda_proyecto_delete, name='agenda_proyecto_delete'),

    url(r'^administracion/estadisticas/$', estadisticas.agenda_estadisticas, name='agenda_estadisticas'),

    url(r'^administracion/cambiar_usuario/$', cuenta.agenda_cambiar_usuario, name='agenda_cambiar_usuario'),
    url(r'^administracion/cambiar_clave/$', cuenta.agenda_cambiar_clave, name='agenda_cambiar_clave'),

    url(r'^administracion/importar/$', importar.agenda_importar, name='agenda_importar'),
    url(r'^administracion/exportar/$', exportar.agenda_exportar, name='agenda_exportar'),

    url(r'^administracion/actividades/comprobar_fechas$',  actividades.agenda_comprobar_fechas_activas, name='agenda_comprobar_fechas_activas'),

]
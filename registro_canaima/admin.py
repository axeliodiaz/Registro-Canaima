# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from registro_canaima.models import *

class PersonasAdmin(admin.ModelAdmin):
    search_fields=['num_identificacion','primer_apellido','primer_nombre','genero']
    list_display=['id','tipodoc','num_identificacion','primer_apellido','segundo_apellido','primer_nombre','segundo_nombre','genero','email']
admin.site.register(Personas,PersonasAdmin)

class CarrerasAdmin(admin.ModelAdmin):
    search_fields=['nombre','personas__num_identificacion']
    list_display=['nombre']
admin.site.register(Carreras,CarrerasAdmin)

# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class Personas(models.Model):
    tipodoc = models.CharField(choices=(('c','Cédula'),('p','Pasaporte')),default=0,max_length=1, verbose_name=u'Tipo de Identificación')
    num_identificacion = models.CharField(max_length=50,unique=True,verbose_name=u'Número de Identificación')
    evento = models.ForeignKey('Evento')
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=20,blank=True)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20,blank=True)
    tipo = models.ForeignKey('TipoPersona', verbose_name='Calidad de')
    genero = models.IntegerField(choices=((0,'Masculino'),(1,'Femenino')),default=0,verbose_name=u'género')
    estado = models.ForeignKey('Estados')
    carrera = models.ForeignKey('Carreras')
    email = models.EmailField()
    telf = models.CharField(max_length=11,blank=True,)
    asist_manana = models.BooleanField(blank=True,verbose_name=u'asistencia en la mañana')
    asist_tarde = models.BooleanField(blank=True,verbose_name=u'asistencia en la tarde')
    class Meta:
        db_table = u'personas'
        verbose_name_plural = 'personas'
    def __unicode__(self):
        return u'(%s) %s %s'%(self.num_identificacion,self.primer_apellido,self.primer_nombre)

class Estados(models.Model):
    nombre = models.CharField(max_length=20)
    class Meta:
        db_table = u'estados'
        verbose_name_plural = 'estados'
    def __unicode__(self):
        return u'%s'%(self.nombre)

class TipoPersona(models.Model):
    tipo = models.CharField(max_length=20)
    class Meta:
        db_table = u'tipo_persona'
        verbose_name_plural = 'tipos de personas'
    def __unicode__(self):
        return u'%s'%(self.tipo)

class Carreras(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        db_table = u'carreras'
        verbose_name_plural = 'carreras'
    def __unicode__(self):
        return u'%s'%(self.nombre)

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField(verbose_name=u'Fecha de inicio')
    fecha_fin = models.DateField(verbose_name=u'Fecha de culminación')
    class Meta:
        db_table = u'evento'
    def __unicode__(self):
        return u'%s'%(self.nombre)


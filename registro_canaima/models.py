# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class Personas(models.Model):
    tipodoc = models.CharField(choices=(('c','Cédula'),('p','Pasaporte')),default=0,max_length=1, verbose_name=u'Tipo de Identificación')
    num_identificacion = models.CharField(max_length=50,unique=True,verbose_name=u'Número de Identificación')
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=20,blank=True)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20,blank=True)
    genero = models.IntegerField(choices=((0,'Masculino'),(1,'Femenino')),default=0,verbose_name=u'sexo')
    carrera = models.ForeignKey('Carreras')
    email = models.EmailField()
    telf = models.CharField(max_length=11,blank=True,)
    asist_manana = models.BooleanField(blank=True)
    asist_tarde = models.BooleanField(blank=True)
    class Meta:
        db_table = u'personas'
        verbose_name_plural = 'personas'
    def __unicode__(self):
        return u'%s %s %s'%(self.num_identificacion,self.primer_apellido,self.primer_nombre)

class Carreras(models.Model):
    nombre = models.CharField(max_length=20)
    class Meta:
        db_table = u'carreras'
        verbose_name_plural = 'carreras'
    def __unicode__(self):
        return u'%s'%(self.nombre)
    

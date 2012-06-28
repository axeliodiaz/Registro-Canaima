#!/bin/sh
# Script que permite la instalación de las aplicaciones necesarias para hacer correr la aplicación

wget http://django-command-extensions.googlecode.com/files/django-extensions-0.4.1.tar.gz -P /tmp/ 
tar xvzf /tmp/django-extensions-0.4.1.tar.gz -C /tmp/
echo "Es necesaria su contraseña para realizar la instalación de aplicaciones..."
su -c "
echo '';

echo 'Actualizando repositorios para iniciar la instalación de aplicaciones'
aptitude update;

echo 'Iniciando la instalación de aplicaciones necesarias y/o importantes para multimedia...';

echo '';

echo 'Iniciando instalación de Django';
aptitude install python-django;

echo 'Iniciando la instalación de PostgreSQL'
aptitude install postgresql;

echo 'Preparando para instalar setup tools. (Ejecuciones de pip install)'; 
aptitude install python-pip; 

echo 'Preparando para instalar python-psycopg2. (Para el motor de PostgreSQL)';
aptitude install python-psycopg2;

echo 'Iniciando la instalación de xdot, un visor de gráficos'; 
aptitude install xdot; 

echo 'Iniciando la instalación de django-extensions';
python /tmp/django-extensions-0.4.1/setup.py install; 

echo 'Iniciando la instalación de Django-qbe';
pip install django_qbe;

echo 'Iniciando la instalación de gource';
pip install gource;
"

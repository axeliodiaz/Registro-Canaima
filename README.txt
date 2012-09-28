Esta es una aplicación para el registro en los eventos en los que pueda estar presente la comunidad Canaima.
La aplicación está desarrollada bajo python con framework django y base de datos postgreSQL.
Para crear la base de datos en PostgreSQL, debemos hacer uso del instalador.sh, éste instalará django, postgresql, python-psycopg2, gource y django_qbe.

=== Configuración de PostgreSQL ===
Para configurar postgres con hacer los siguientes comandos:
$ su 
# su postgres
# createuser -P registro; createdb registro_canaima -O registro
Con esto, debemos tener listo el usuario y contraseña del PostgreSQL con la base de datos configurada con este sistema. (Recordar configurar el pg_hba.conf)

=== Configuración de Django ===
Una vez tenido el código fuente, para iniciar el sistema se debe ejecutar:

$ ./manage.py syncdb; ./manage.py runserver

De esta manera sincronizamos la base de datos y posteriormente, iniciamos el servidor.
El sistema puede verse vía web en http://localhost:8000/

Instalar Themes para el admin de django: 

pip install django-grappelli

Luego hacer un COLLECTSTATIC

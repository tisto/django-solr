Django Solr Starter
===================

Django
------

Python Setup::

  $ virtualenv .env
  $ source .env/bin/activate
  $ pip install -r requirements.txt

Create Django App::

  $ django-admin startproject mysite
  $ (cd mysite && python manage migrate)

Create Superuser::

  $ python manage.py createsuperuser

Start Django::

  $ (cd mysite && python manage runserver)


Java
----

Download Java 8::

  $ wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u111-b14/jre-8u111-linux-x64.tar.gz
  $ tar xfvz jre-8u111-linux-x64.tar.gz

Install Java 8::

  $ sudo mv jre1.8.0_111/ /opt
  $ sudo mv jre1.8.0_111/ /opt/Oracle_Java/jre1.8.0_8u111/
  $ sudo update-alternatives --install "/usr/bin/java" "java" "/opt/jre1.8.0_111/bin/java" 1
  $ sudo update-alternatives --install "/usr/bin/javaws" "java" "/opt/jre1.8.0_111/bin/javaws" 1
  $ sudo update-alternatives --set "java" "/opt/jre1.8.0_111/bin/java"
  $ sudo update-alternatives --set "javaws" "/opt/jre1.8.0_111/bin/javaws"


Solr
----

Download and install::

  $ wget http://apache.mirror.digionline.de/lucene/solr/6.3.0/solr-6.3.0.tgz
  $ tar xfvz solr-6.3.0.tgz

Create Solr core::

  $ cp example/files/conf/solrconfig.xml django/
  $ cp example/files/conf/managed-schema django/
  $ cp example/files/conf/elevate.xml django/
  $ cp example/files/conf/update-script.js django/
  $ bin/solr create_core -c django -d django/

Delete Solr core::

  $ bin/solr delete -c django

"""Gestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^carreras&especialidades/', include('apps.carreras.urls')),
    url(r'^atributos/', include('apps.atributos.urls')),
    url(r'^profesores/', include('apps.profesores.urls')),
    url(r'^alumnos/', include('apps.alumnos.urls')),
    url(r'^grupos/', include('apps.grupos.urls')),
    url(r'^SIEVAT/', include('apps.inicio.urls')),
]

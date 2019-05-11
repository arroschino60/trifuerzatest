from django.conf.urls import url

from apps.inicio.views import inicio

urlpatterns = [
    url(r'^$', inicio, name='SIEVAT'),
    ]
from django.conf.urls import url

from apps.carreras.views import mostrarCE, mostrarCarrera, registrarCarrera, registrarEspecialidad, carreraUpdate, especialidadUpdate, carreraDelete, especialidadDelete

urlpatterns = [
    url(r'^$', mostrarCarrera, name='carrera'),
    url(r'^RegistrarCarrera$', registrarCarrera.as_view(), name='carreraRegistrar'),
    url(r'^editarcarrera/(?P<pk>\d+)/$', carreraUpdate.as_view(), name='carreraModificar'),
    url(r'^eliminarcarrera/(?P<pk>\d+)/$', carreraDelete.as_view(), name='carreraEliminar'),
    url(r'^RegistrarEspecialidad$', registrarEspecialidad.as_view(), name='especialidadRegistrar'),
    url(r'^editarespecialidad/(?P<pk>\d+)/$', especialidadUpdate.as_view(), name='especialidadModificar'),
    url(r'^eliminarespecialidad/(?P<pk>\d+)/$', especialidadDelete.as_view(), name='especialidadEliminar'),
]
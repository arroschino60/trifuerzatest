from django.conf.urls import url

from apps.profesores.views import mostrarProfesor, registrarProfesor, profesorUpdate, profesorDelete

urlpatterns = [
    url(r'^$', mostrarProfesor.as_view(), name='profesores'),
    url(r'^nuevo', registrarProfesor.as_view(), name='profesorRegistrar'),
    url(r'^editar/(?P<pk>\d+)/$', profesorUpdate.as_view(), name='profesorModificar'),
    url(r'^eliminar/(?P<pk>\d+)/$', profesorDelete.as_view(), name='profesorEliminar'),
    ]
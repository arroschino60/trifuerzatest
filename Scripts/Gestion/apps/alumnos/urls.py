from django.conf.urls import url

from apps.alumnos.views import mostrarA, registrarAlumno, alumnoUpdate, alumnoDelete

urlpatterns = [
    url(r'^$', mostrarA, name='alumnos'),
    url(r'^nuevo', registrarAlumno.as_view(), name='alumnoRegistrar'),
    url(r'^editar/(?P<pk>\d+)/$', alumnoUpdate.as_view(), name='alumnoModificar'),
    url(r'^eliminar/(?P<pk>\d+)/$', alumnoDelete.as_view(), name='alumnoEliminar'),
    ]
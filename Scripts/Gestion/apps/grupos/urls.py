from django.conf.urls import url

from apps.grupos.views import mostrarGrupo, registrarGrupo, grupoUpdate, grupoDelete

urlpatterns = [
    url(r'^$', mostrarGrupo.as_view(), name='grupos'),
    url(r'^nuevo', registrarGrupo.as_view(), name='grupoRegistrar'),
    url(r'^editar/(?P<pk>\d+)/$', grupoUpdate.as_view(), name='grupoModificar'),
    url(r'^eliminar/(?P<pk>\d+)/$', grupoDelete.as_view(), name='grupoEliminar'),
    ]
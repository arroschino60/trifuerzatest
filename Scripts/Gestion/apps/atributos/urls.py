from django.conf.urls import url

from apps.atributos.views import mostrarAtributos, registrarAtributo, atributoUpdate, atributoDelete,registrarCriterio

urlpatterns = [
    url(r'^$', mostrarAtributos.as_view(), name='atributos'),
    url(r'^nuevo', registrarAtributo.as_view(), name='atributoRegistrar'),
    url(r'^editar/(?P<pk>\d+)/$', atributoUpdate.as_view(), name='atributoModificar'),
    url(r'^eliminar/(?P<pk>\d+)/$', atributoDelete.as_view(), name='atributoEliminar'),
    url(r'^criterio$', registrarCriterio.as_view(), name='criterioVincular'),
    ]
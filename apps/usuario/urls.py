from django.conf.urls import url

from apps.usuario.views import RegistroUsuario, SolicitudRegistro, SolicitudDelete

urlpatterns = [
	url(r'^registrar',RegistroUsuario.as_view(),name="registrar"),
	url(r'^listar$', SolicitudRegistro.as_view(), name='usuario_listar'),
	url(r'^eliminar/(?P<pk>\d)$',SolicitudDelete.as_view(), name='usuario_eliminar'),
]
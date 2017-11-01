from django.conf.urls import url

from apps.usuario.views import RegistroUsuario, SolicitudRegistro, SolicitudDelete, Selecccion, Egresado, Administrador

urlpatterns = [
	url(r'^registrar',RegistroUsuario.as_view(),name="registrar"),
	url(r'^seleccion',Selecccion,name="seleccion"),
	url(r'^listar$', SolicitudRegistro.as_view(), name='usuario_listar'),
	url(r'^eliminar/(?P<pk>\d)$',SolicitudDelete.as_view(), name='usuario_eliminar'),
	url(r'^egresado$', Egresado, name='egresado_index'),
	url(r'^administrador$', Administrador, name='administrador_index'),
]
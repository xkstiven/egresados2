from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.usuario.views import RegistroUsuario, SolicitudRegistro, SolicitudDelete, Selecccion, Egresado, Administrador, SolicitudAceptar

urlpatterns = [
	url(r'^registrar',RegistroUsuario.as_view(),name="registrar"),
	url(r'^seleccion',Selecccion,name="seleccion"),
	url(r'^aceptar/(?P<pk>\d)$',login_required(SolicitudAceptar.as_view()),name="usuario_aceptar"),
	url(r'^listar$', login_required(SolicitudRegistro.as_view()), name='usuario_listar'),
	url(r'^eliminar/(?P<pk>\d)$',login_required(SolicitudDelete.as_view()), name='usuario_eliminar'),
	url(r'^egresado$', login_required(Egresado), name='egresado_index'),
	url(r'^administrador$', login_required(Administrador), name='administrador_index'),
]
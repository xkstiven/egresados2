from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.usuario.views import RegistroUsuario, SolicitudAceptarADM,SolicitudRegistro, SolicitudDelete, Selecccion, EgresadoP, Administrador, SolicitudAceptar, SolicitudAdmin,Super, change_password,cambio

urlpatterns = [
	url(r'^registrar',RegistroUsuario.as_view(),name="registrar"),
	url(r'^seleccion',Selecccion,name="seleccion"),
	url(r'^aceptar/(?P<id_usuario>\d)$',login_required(SolicitudAceptar),name="usuario_aceptar"),
	url(r'^aceptarADM/(?P<pk>\d)$',login_required(SolicitudAceptarADM.as_view()),name="admin_aceptar"),
	url(r'^listar$', login_required(SolicitudRegistro.as_view()), name='usuario_listar'),
	url(r'^listadm$', login_required(SolicitudAdmin.as_view()), name='admin_listar'),
	url(r'^eliminar/(?P<pk>\d)$',login_required(SolicitudDelete.as_view()), name='usuario_eliminar'),
	url(r'^egresado/$', login_required(EgresadoP), name='egresado_index'),
	url(r'^administrador$', login_required(Administrador), name='administrador_index'),
	url(r'^super$', login_required(Super), name='super_index'),
	url(r'^cambio$', login_required(cambio), name='cambio'),
	url(r'^password/$',login_required(change_password),name='change_password'),
]
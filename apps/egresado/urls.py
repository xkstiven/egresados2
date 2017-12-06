from django.conf.urls import url, include
from apps.egresado.views import EgresadoCrear, EgresadoList, EgresadoUpdate2, EgresadoEliminar, InteresCrear, amigo_solicitar
from django.contrib.auth.decorators import login_required

from apps.egresado.views import AmigoAceptar, amigo_solicitudes, amigos, vista, amigo_sugerencia,vistaMi,Avatar

urlpatterns=[
	url(r'^nuevo$',login_required(EgresadoCrear.as_view()),name='egresado_crear'),
	url(r'^listar$',login_required(EgresadoList.as_view()),name='egresado_listar'),
	url(r'^editar/(?P<id_egresado>\d+)/$', login_required(EgresadoUpdate2), name='egresado_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(EgresadoEliminar.as_view()), name='egresado_eliminar'),
    url(r'^agregar/(?P<id_egresado>\d+)/$', login_required(amigo_solicitar), name='amigo_agregar'),
    url(r'^nuevoInt$', login_required(InteresCrear.as_view()), name='interes_crear'),
    url(r'^aceptar/(?P<pk>\d+)/$', login_required(AmigoAceptar.as_view()), name='amigo_aceptar'),
    url(r'^solicitudes$', login_required(amigo_solicitudes.as_view()), name='solicitudes'),
    url(r'^amigos$', login_required(amigos.as_view()), name='amigos'),
    url(r'^vista/(?P<pk>\d+)/$', login_required(vista.as_view()), name='vista'),
    url(r'^vistaMi/(?P<pk>\d+)/$', login_required(vistaMi.as_view()), name='vistami'),
    url(r'^avatar/(?P<pk>\d+)/$', login_required(Avatar), name='avatar'),
    url(r'^sugerencia$', login_required(amigo_sugerencia.as_view()), name='sugerencia'),
]
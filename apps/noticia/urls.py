from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.noticia.views import crear_noticia , noti_lista, noti

urlpatterns = [
	url(r'^crear$',login_required(crear_noticia),name="nueva"),
	url(r'^listar$',login_required(noti_lista.as_view()),name="listar"),
	url(r'^ver/(?P<pk>\d)$',login_required(noti.as_view()), name='ver_noticia'),
]

#url(r'^eliminar/(?P<pk>\d)$',login_required(SolicitudDelete.as_view()), name='usuario_eliminar'),

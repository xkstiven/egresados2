from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect


from apps.usuario.forms import RegistroForm, Perfil

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('login')

class SolicitudAceptar(UpdateView):
	model= User
	form_class = Perfil
	template_name= 'usuario/aceptar.html'
	success_url= reverse_lazy('usuario:usuario_listar')

class SolicitudRegistro(ListView):
	model = User
	template_name= 'usuario/usuario_list.html'

	def get_queryset(self):
		return User.objects.filter(is_active=False)

class SolicitudDelete(DeleteView):
	model = User
	template_name ='usuario/usuario_delete.html'
	seccess_url = reverse_lazy('usuario/usuario_list.html')

def Selecccion(request):
	return render(request,'usuario/seleccion.html')

def Egresado(request):
	return render(request,'egresado/index.html')

def Administrador(request):
	return render(request,'usuario/admIndex.html')
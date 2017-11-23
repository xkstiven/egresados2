from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from apps.egresado.models import Egresado



from apps.usuario.forms import RegistroForm, Perfil

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user,request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'clave cambiada con exito')
			return redirect('logout')
		else:
			messages.error(request,'contraseña invalida')
	else:
		form = PasswordChangeForm(request.user)
	return render(request,'usuario/change_password.html',{'form':form})

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('principal')

class SolicitudAceptar(UpdateView):
	model= User
	form_class = Perfil
	template_name= 'usuario/aceptar.html'
	success_url= reverse_lazy('usuario:usuario_listar')

class SolicitudRegistro(ListView):
	model = User
	template_name= 'usuario/usuario_list.html'

	def get_queryset(self):
		return User.objects.filter(is_staff=False).filter(is_active=False)

class SolicitudAdmin(ListView):
	model = User
	template_name = 'usuario/admin_list.html'

	def get_queryset(self):
		return User.objects.filter(is_staff=True).filter(is_active=False)

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

def Super(request):
	return render(request,'usuario/super_Index.html')

def cambio(request):
	return render(request,'usuario/cambio.html')
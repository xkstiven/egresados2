from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from .forms import LoginForm
from django.contrib.auth import authenticate, login

def principal(request):
	return render(request,'principal.html')

def login_page(request):
	message = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active and user.is_staff:
					login(request,user)
					message = "ingresado como administrador"
					return render(request,'usuario/admIndex.html')
				elif user.is_active:
					login(request,user)
					message = "ingresado como egresado"
					return render(request,'egresado/index.html')
				else:
					message = "usuario inactivo"
			else:
				message = "Nombre de usuario y/o contraseña incorrectos"
	else:
		form = LoginForm()
	return render_to_response('login.html',{'message':message,'form':form},context_instance=RequestContext(request))
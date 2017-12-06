from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from apps.egresado.forms import EgresadoForm, InteresForm, AmigoForm, AmigoAcep, CambioAvatar
from apps.egresado.models import Egresado, Interes, Amigos
from django.contrib.auth.models import User
from itertools import chain
# Create your views here.

class vista(DetailView):
	model = Egresado
	template_name = 'egresado/vista.html'

class vistaMi(DetailView):
	model = Egresado
	template_name = 'egresado/vistaMi.html'


def amigo_solicitar(request,id_egresado):
	if request.method =='POST':
		crea = request.user
		persona = User.objects.get(id=crea.id)
		amigo= Egresado.objects.get(id=id_egresado)
		form = AmigoForm(request.POST)
		if form.is_valid():
			persona = persona
			first_name = crea.first_name
			last_name= crea.last_name
			amigo=amigo
			aceptado = form.cleaned_data['aceptado']
			Amigos.objects.create(persona=persona,first_name=first_name,last_name=last_name,amigo=amigo,aceptado=aceptado)
		return redirect ('usuario:egresado_index')
	else:
		form = AmigoForm()
	return render(request,'egresado/amigo.html',{'form':form})

def Avatar(request,pk):
	egresado = Egresado.objects.get(id=pk)
	if request.method == 'GET':
		form = CambioAvatar(instance=egresado)
	else:
		form = CambioAvatar(request.POST,request.FILES,instance=egresado)
		if form.is_valid():
			form.save()
		return redirect('egresado:vistami',pk=request.user.id)
	return render (request,'egresado/avatar.html',{'form':form})

def EgresadoUpdate2(request,id_egresado):
	egresado = Egresado.objects.get(id=id_egresado)
	if request.method == 'GET':
		form = EgresadoForm(instance=egresado)
	else:
		form = EgresadoForm(request.POST,instance=egresado)
		if form.is_valid():
			form.save()
			e= Egresado.objects.get(id=id_egresado)
			e.usuario_id = request.user
			e.save()
		return redirect('egresado:vistami',pk=request.user.id)
	return render(request,'egresado/egresado_form.html',{'form':form})

class EgresadoUpdate(UpdateView):
	model = Egresado
	form_class= EgresadoForm
	template_name= 'egresado/egresado_form.html'
	success_url = reverse_lazy('usuario:egresado_index')


class amigo_solicitudes(ListView):
	model = Amigos
	template_name = 'egresado/solicitudes.html'

	def get_queryset(self):
		return Amigos.objects.filter(amigo_id=self.request.user.id).filter(aceptado=False)

class amigo_sugerencia(ListView):
	model = Egresado
	template_name = 'egresado/enviar.html'

	def get_queryset(self):
		egres = Egresado.objects.get(id=self.request.user.id)
		filcarr = Egresado.objects.filter(carrera_id=egres.carrera_id).exclude(id=egres.id).exclude(usuario=None)
		filanyo = Egresado.objects.filter(grado=egres.grado).exclude(id=egres.id).exclude(usuario=None)
		return (filcarr|filanyo).distinct().order_by('id')

class amigos(ListView):
	model = Amigos
	template_name = 'egresado/Amigos.html'

	def get_queryset(self):
		return Amigos.objects.filter(amigo_id=self.request.user.id).filter(aceptado=True)


class AmigoAceptar(UpdateView):
	model = Amigos
	form_class= AmigoForm
	template_name = 'egresado/amigoacept.html'
	success_url = reverse_lazy('usuario:egresado_index')

class EgresadoCrear(CreateView):
	model = Egresado
	form_class = EgresadoForm
	template_name = 'egresado/egresado_form.html'
	success_url = reverse_lazy('egresado:egresado_listar')

class InteresCrear(CreateView):
	model = Interes
	form_class = InteresForm
	template_name='egresado/interes_form.html'
	success_url= reverse_lazy('usuario:super_index')

class EgresadoList(ListView):
	model = Egresado
	template_name= 'egresado/egresado_list.html'


class EgresadoEliminar(DeleteView):
	model = Egresado
	template_name= 'egresado/egresado_delete.html'
	success_url= reverse_lazy('egresado:egresado_listar')
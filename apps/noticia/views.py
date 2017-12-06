from django.shortcuts import render, redirect
from apps.noticia.forms import Noticia_Crear
from apps.noticia.models import Noticia
from apps.egresado.models import Egresado
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# Create your views here.

def crear_noticia(request):
	if request.method == 'POST':
		form = Noticia_Crear(request.POST)
		if form.is_valid():
			desc_corta = form.cleaned_data['desc_corta']
			descripcion = form.cleaned_data['descripcion']
			interes = form.cleaned_data['interes']
			Noticia.objects.create(desc_corta=desc_corta,descripcion=descripcion,interes=interes)
			asunto = 'Nueva noticia'
			mensaje= 'hay una nueva noticia en la plataforma con uno de tus intereses'
			#mail = EmailMessage(asunto,mensaje,to=[usuario.email])
			#mail.send()
		return redirect('usuario:administrador_index')
	else:
		form = Noticia_Crear()
	return render(request,'noticia/noticia_form.html',{'form':form})

class noti(DetailView):
	model = Noticia
	template_name = 'noticia/noticia.html'

class noti_lista(ListView):
	model = Noticia
	template_name= 'noticia/listar.html'

	def get_queryset(self):
		return Noticia.objects.all().order_by('-id')
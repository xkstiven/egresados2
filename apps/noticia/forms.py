from django import forms

from apps.egresado.models import Interes
from apps.noticia.models import Noticia

class Noticia_Crear(forms.ModelForm):
	class Meta:
		model= Noticia
		fields=['desc_corta','descripcion','interes']
		labels= {
			'desc_corta': 'Descripcion corta',
			'descripcion':'Descripcion completa',
			'interes':'interes',
			}
		widgets={
			'desc_corta':forms.Textarea(attrs={'class':'form-control'}),
			'descripcion':forms.Textarea(attrs={'class':'form-control'}),
			'interes':forms.Select(attrs={'class':'form-control'}),
		}

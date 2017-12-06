from django.db import models
from apps.egresado.models import Interes


class Noticia(models.Model):
	desc_corta= models.TextField()
	descripcion = models.TextField()
	interes = models.ForeignKey(Interes,null=True,blank=True)
	#multimedia = models.FileField(upload_to='medias',blank=True, null=True)
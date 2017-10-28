from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Interes(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class Sexo(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class Pais(models.Model):
	nombre = models.CharField(max_length= 50)

	def __str__(self):
		return '{}'.format(self.nombre)

class Departamento(models.Model):
	nombre = models.CharField(max_length= 50)
	pais = models.ForeignKey(Pais,null=False,blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)

class Carrera(models.Model):
	nombre = models.CharField(max_length= 50)

	def __str__(self):
		return '{}'.format(self.nombre)

class Egresado(models.Model):
	usuario= models.ForeignKey(User,null=True,blank=True)
	nombre= models.CharField(max_length=50,null=True)
	apellidos = models.CharField(max_length= 100,null=True)
	codigo = models.CharField(max_length=10,null=True)
	fecha_nacimiento = models.DateField(null=True)
	carrera = models.ForeignKey(Carrera,null=True,blank=True)
	grado= models.IntegerField(null=True)
	sexo= models.ForeignKey(Sexo,null=True,blank=True)
	departamento= models.ForeignKey(Departamento,null=True,blank=True)
	pais= models.ForeignKey(Pais,null=True,blank=True)
	interes = models.ManyToManyField(Interes,null=True,blank=True)
	administrador = models.BooleanField()
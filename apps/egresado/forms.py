from django import forms

from apps.egresado.models import Egresado, Interes, Amigos


class AmigoForm(forms.ModelForm):
	class Meta:
		model = Amigos
		fields = ['aceptado']
		
class AmigoAcep(forms.ModelForm):
	class Meta:
		model = Amigos
		fields=['persona','first_name','last_name','amigo','aceptado']
		widgets={'aceptado':forms.CheckboxInput()}

class InteresForm(forms.ModelForm):
	class Meta:
		model = Interes
		fields=['nombre']
		labels= {'nombre':'Nombre'}
		widgets={'nombre':forms.TextInput(attrs={'class':'form-control'})}

class EgresadoFormAdm(forms.ModelForm):
	
	class Meta:
		model = Egresado

		fields = [
			'usuario',
			'codigo',
			'fecha_nacimiento',
			'carrera',
			'grado',
			'sexo',
			'pais',
			'departamento',
			'interes',
		]

		labels = {
			'usuario':'Usuario',
			'codigo': 'Cedula',
			'fecha_nacimiento':'Fecha Nacimiento',
			'carrera':'Carrera',
			'grado':'anyo graduacion',
			'sexo':'Sexo',
			'pais':'Pais',
			'departamento':'Departamento',
			'interes':'Interes',
		}

		widgets={
		'usuario':forms.Select(attrs={'class':'form-control'}),
		'codigo': forms.TextInput(attrs={'class':'form-control'}),
		'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control'}),
		'carrera':forms.Select(attrs={'class':'form-control'}),
		'sexo':forms.Select(attrs={'class':'form-control'}),
		'grado':forms.TextInput(attrs={'class':'form-control'}),
		'pais':forms.Select(attrs={'class':'form-control'}),
		'departamento':forms.Select(attrs={"name":"select_0",'class':'form-control'}),
		'interes':forms.CheckboxSelectMultiple(),
		}

class EgresadoForm(forms.ModelForm):
	
	class Meta:
		model = Egresado

		fields = [
			'codigo',
			'fecha_nacimiento',
			'carrera',
			'grado',
			'sexo',
			'pais',
			'departamento',
			'interes',
		]

		labels = {
			'codigo': 'Cedula',
			'fecha_nacimiento':'Fecha Nacimiento',
			'carrera':'Carrera',
			'grado':'anyo graduacion',
			'sexo':'Sexo',
			'pais':'Pais',
			'departamento':'Departamento',
			'interes':'Interes',
		}

		widgets={
		'codigo': forms.TextInput(attrs={'class':'form-control'}),
		'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control'}),
		'carrera':forms.Select(attrs={'class':'form-control'}),
		'sexo':forms.Select(attrs={'class':'form-control'}),
		'grado':forms.TextInput(attrs={'class':'form-control'}),
		'pais':forms.Select(attrs={'class':'form-control'}),
		'departamento':forms.Select(attrs={"name":"select_0",'class':'form-control'}),
		'interes':forms.CheckboxSelectMultiple(),
		}



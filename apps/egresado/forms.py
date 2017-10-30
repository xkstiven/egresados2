from django import forms

from apps.egresado.models import Egresado

class EgresadoFormAdm(forms.ModelForm):
	
	class Meta:
		model = Egresado

		fields = [
			'usuario',
			'nombre',
			'apellidos',
			'codigo',
			'fecha_nacimiento',
			'carrera',
			'grado',
			'sexo',
			'pais',
			'departamento',
			'interes',
			'administrador',
		]

		labels = {
			'usuario':'Usuario',
			'nombre':'Nombre',
			'apellidos': 'Apellidos',
			'codigo': 'Cedula',
			'fecha_nacimiento':'Fecha Nacimiento',
			'carrera':'Carrera',
			'grado':'anyo graduacion',
			'sexo':'Sexo',
			'pais':'Pais',
			'departamento':'Departamento',
			'interes':'Interes',
			'administrador':'desea enviar solicitud apra ser un administrador del sistema',
		}

		widgets={
		'usuario':forms.Select(attrs={'class':'form-control'}),
		'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'apellidos':forms.TextInput(attrs={'class':'form-control'}),
		'codigo': forms.TextInput(attrs={'class':'form-control'}),
		'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control'}),
		'sexo':forms.Select(attrs={'class':'form-control'}),
		'grado':forms.TextInput(attrs={'class':'form-control'}),
		'pais':forms.Select(attrs={'class':'form-control'}),
		'departamento':forms.Select(attrs={"name":"select_0",'class':'form-control'}),
		'interes':forms.CheckboxSelectMultiple(),
		'administrador':forms.CheckboxInput(),
		}

class EgresadoForm(forms.ModelForm):
	
	class Meta:
		model = Egresado

		fields = [
			'nombre',
			'apellidos',
			'codigo',
			'fecha_nacimiento',
			'carrera',
			'grado',
			'sexo',
			'pais',
			'departamento',
			'interes',
			'administrador',
		]

		labels = {
			'nombre':'Nombre',
			'apellidos': 'Apellidos',
			'codigo': 'Cedula',
			'fecha_nacimiento':'Fecha Nacimiento',
			'carrera':'Carrera',
			'grado':'anyo graduacion',
			'sexo':'Sexo',
			'pais':'Pais',
			'departamento':'Departamento',
			'interes':'Interes',
			'administrador':'desea enviar solicitud apra ser un administrador del sistema',
		}

		widgets={
		'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'apellidos':forms.TextInput(attrs={'class':'form-control'}),
		'codigo': forms.TextInput(attrs={'class':'form-control'}),
		'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control'}),
		'sexo':forms.Select(attrs={'class':'form-control'}),
		'grado':forms.TextInput(attrs={'class':'form-control'}),
		'pais':forms.Select(attrs={'class':'form-control'}),
		'departamento':forms.Select(attrs={"name":"select_0",'class':'form-control'}),
		'interes':forms.CheckboxSelectMultiple(),
		'administrador':forms.CheckboxInput(),
		}
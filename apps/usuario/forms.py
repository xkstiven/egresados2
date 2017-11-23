from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from django import forms

class RegistroForm(UserCreationForm):
	captcha = ReCaptchaField(widget=ReCaptchaWidget(attrs={'class':'validate'}),label="")

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
				'is_active',
				'is_staff',
			]
		labels = {
				'username': 'Nombre usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email':'Confirme correo',
				'is_active': 'activo',
				'is_staff':'Perfil como Administrador?'
		}
		widgets={
		}

# con esta clase modificamos aceptamos los perfiles de administrador o egresado
class Perfil(forms.ModelForm):    
	class Meta:
		model = User
		fields = ['is_active']
		labels = {'is_active':'activar'}
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
				'email',
				'is_active',
			]
		labels = {
				'username': 'Nombre usuario',
				'email':'Confirme correo',
				'is_active': 'activo',

		}
		widgets={
		}
		
class Perfil(forms.ModelForm):
	class Meta:
		model = User
		fields = ['is_active']
		labels = {'is_active':'activar'}
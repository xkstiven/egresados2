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
			]
		labels = {
				'username': 'Nombre usuario',
				'email':'Confirme correo',

		}
		widgets={
		}

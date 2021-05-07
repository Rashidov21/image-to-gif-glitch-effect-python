from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ["username","first_name",'last_name', "email", "password1", "password2"]
		widgets = {
			
		}

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'
		exclude = ('user',)
		widgets = {
			
		}

from django import forms 
from .models import Contact


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
			'email':forms.EmailInput(attrs={'class':'form-control'})
		}
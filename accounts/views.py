from django.shortcuts import render
from .forms import *
# Create your views here.


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form =RegisterForm()
		print('$'*20)
	return render(request, 'accounts/register.html', {'form':form})
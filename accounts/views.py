from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from .models import UserProfile
from django.urls import reverse
# Create your views here.


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			u = User.objects.last()
			UserProfile.objects.create(user=u)
			return render(request, 'index.html')
	else:
		form = RegisterForm()
		print('$'*20)
		return render(request, 'accounts/register.html', {'form':form})
	return render(request, 'accounts/register.html', {'form':form})

def profile(request):
	return render(request, 'profile.html')
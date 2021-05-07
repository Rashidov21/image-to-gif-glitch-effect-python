from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from .models import UserProfile
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# CRUD - Create , Update , Delete
# CRUD meros oladigan classlar > TemplateResponsoMixin, FormView
class CreatePostView(CreateView):
	model = TestPost
	fields = ['title', 'body']
	success_url = '/'


class UpdatePostView(UpdateView):
	model = TestPost
	fields = ['title', 'body']
	success_url = '/'


class DeletePostView(DeleteView):
	model = TestPost
	fields = ['title', 'body']
	success_url = '/'

class ListPostView(ListView):
	model = TestPost
	template_name = 'posts.html'

class DetailPostView(DetailView):
	model = TestPost
	template_name = 'posts.html'

# Create your views here.
class ProfileCreateView(CreateView):
	model = UserProfile
	fields =['image', 'address', 'brth']
	success_url = '/accounts/profile/'
	template_name = 'profile.html'


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


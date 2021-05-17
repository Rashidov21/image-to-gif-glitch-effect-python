from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from django.contrib.auth.models import User
from .models import UserProfile
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# CRUD - Create , Update , Delete
# CRUD meros oladigan classlar > TemplateResponsoMixin, FormView
class CreatePostView(LoginRequiredMixin,CreateView):
	model = TestPost
	fields = ['title', 'body']
	login_url = 'accounts:login'
	# redirect_field_name = 'redirect_to'
	success_url = '/'

class UpdatePostView(LoginRequiredMixin,UpdateView):
	model = TestPost
	fields = ['title', 'body']
	login_url = 'accounts:login'
	success_url = '/'

# delete view for details
@login_required
def delete_view(request, obj_id):
	context ={}

	obj = get_object_or_404(TestPost, id=obj_id)

	if request.method =="POST":
		# delete object
		obj.delete()
		# after deleting redirect to
		# home page
		return HttpResponseRedirect("/")

	return render(request, "delete.html", context)




class ListPostView(ListView):
	model = TestPost
	template_name = 'posts.html'



class DetailPostView(DetailView):
	model = TestPost
	template_name = 'posts.html'

# Create your views here.
def user_profile(request):
	print(request.user.user_profile.__dir__())
	if request.method == 'POST':
		update_form = ProfileUpdateForm(request.POST)
		if update_form.is_valid():
			update_form.save()
			print('*'*50)
		else:
			print('#'*50)
	else:
		update_form = ProfileUpdateForm()
	# print(request.user.__dir__())
	return render(request, 'accounts/profile.html', {'update_form':update_form})

# class ProfileCreateView(CreateView):
# 	model = UserProfile
# 	fields =['image', 'address', 'brth']
# 	success_url = '/accounts/profile/'
# 	template_name = 'accounts/profile.html'
	


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


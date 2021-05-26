from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from django.contrib.auth.models import User
from .models import UserProfile
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
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
class UserProfile(LoginRequiredMixin,UpdateView):
	model = UserProfile
	fields = ['image', 'address','brth']
	success_url = '/'
	template_name = 'accounts/profile.html'

	# def get(self,request):
	# 	# if request.user.is_authenticated:
	# 	# 	messages.success(request, "Siz ro'yxatdan o'tgansiz!")
	# 	# 	return redirect('game:homePage')
	# 	form = ProfileUpdateForm()
	# 	context = {'form':form}
	# 	return render(request, 'accounts/profile.html', context)

	# def post(self,request):
	# 	form = ProfileUpdateForm(request.POST)
	# 	if form.is_valid():
			
	# 		try:
	# 			u = request.user
	# 			image = request.POST['image']
	# 			address = request.POST['address']
	# 			brth = request.POST['brth']
	# 			use = UserProfile.objects.create(
	# 				user=u,image=image, 
	# 				address=address,brth=brth)

	# 		except:
	# 			use = None
	# 		messages.success(request, 'Tabriklaymiz ' + u.first_name + '  siz muvaffiqiyatli ro\'yhatdan o\'tdingiz!')
	# 		form.save()
	# 		return redirect('game:homePage')
	# 	else:
	# 		form = ProfileUpdateForm()
	# 	context = {'form':form}
	# 	return render(request, 'accounts/profile.html', context)




# class ProfileCreateView(CreateView):
# 	model = UserProfile
# 	fields =['image', 'address', 'brth']
# 	success_url = '/accounts/profile/'
# 	template_name = 'accounts/profile.html'
	


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			u = form.save()
			try:
				user = UserProfile.objects.create(user=u)
				user.save()
			except:
				user = None
			return redirect('accounts:profile')

	else:
		form = RegisterForm()
		print('$'*20)
		return render(request, 'accounts/register.html', {'form':form})
	return render(request, 'accounts/register.html', {'form':form})


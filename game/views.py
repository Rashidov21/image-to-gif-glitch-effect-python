from django.shortcuts import render  
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.db.models import Q

from .forms import ContactForm

from .models import Game
# from .models import contact
# Create your views here.

class HomeView(ListView):
	# Home Page View controller class
	model = Game
	queryset = Game.objects.all()
	context_object_name = 'games'
	template_name = 'index.html'

	# def get_context_data(self, **kwargs):
	# 	# Call the base implementation first to get a context
	# 	context = super().get_context_data(**kwargs)
	# 	# Add in a QuerySet of all the games
	# 	context['games'] = Game.objects.all()
	# 	return context

	# def get(self, request):
	# 	return render(request, 'index.html')
# Upakovka
# *args  = arguments => set()
# **kwargs = keyword arguments => dict()

class GameDetailView(DetailView):
	model = Game
	template_name = 'single.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

# YourTable.phone => prefix => id_ == id_phone 


# Create your views here.
class ContactView(View):

	def get(self,request):
		form = ContactForm()
		return render(request, 'contact.html', {'form':form})

	def post(self, request):
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			print('*'*50)
		else:
			form = ContactForm()
			print('#'*50)
		return render(request, 'contact.html', {'form':form})






def search (request):
	query = request.GET.get('search')
	posts = Post.objects.filter(
		Q(title_icontains=query) & Q(body__icontains=query)
		)

	context = {
		'index':posts
	}
	return render(request, 'index.html', context)




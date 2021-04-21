from django.shortcuts import render

from django.views.generic.base import View

# Create your views here.

class HomeView(View):
	# Home Page View controller class
	def get(self, request):
		return render(request, 'index.html')
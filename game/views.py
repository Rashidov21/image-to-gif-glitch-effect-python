from django.shortcuts import render  
from django.views.generic import ListView
from django.db.models import Q

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

# Create your views here.
def contact(request):
	if request.method == 'POST':
		n = request.POST['name']
		e = request.POST['email']
		s = request.POST['subject']
		m = request.POST['message']
		contact.objects.create(name=n, email=e,subject=s, message=m,)
		print('#'*50)
	else:
		print('error'*10)	
	return render(request, 'contact.html')


def search (request):
	query = request.GET.get('search')
	posts = Post.objects.filter(
		Q(title_icontains=query) & Q(body__icontains=query)
		)

	context = {
		'index':posts
	}
	return render(request, 'index.html', context)



def games(request):

	return render(request,'games.html')

def news(request):

	return render(request,'404.html')


def blog(request):

	return render(request,'blog.html')
def reviews(request):

	return  render(request,'reviews.html')

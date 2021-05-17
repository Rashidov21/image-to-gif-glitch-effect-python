from django.urls import path 
from .import views

app_name = 'game'

urlpatterns = [
	path('', views.HomeView.as_view(), name='homePage'),
	path('contact', views.contact, name='contact'),
	path('games', views.games, name='games'),
	path('reviews',views.reviews, name='reviews'),
	path('news', views.news, name='news'),
	path('blog',views.blog,name='blog'),
	path('search', views.search, name='search')
]
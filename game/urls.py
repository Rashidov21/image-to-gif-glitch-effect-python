from django.urls import path 
from .import views

app_name = 'game'

urlpatterns = [
	path('', views.HomeView.as_view(), name='homePage'),
	path('contact', views.ContactView.as_view(), name='contact'),
	path('<slug:slug>/', views.GameDetailView.as_view(), name='detail'),

	path('search', views.search, name='search')
]
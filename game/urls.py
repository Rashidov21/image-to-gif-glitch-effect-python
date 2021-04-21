from django.urls import path 
from .import views

app_name = 'game'

urlpatterns = [
	path('', views.HomeView.as_view(), name='homePage')
]
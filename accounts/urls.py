from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from .import views

app_name = 'accounts'

urlpatterns = [
	path('login/', LoginView.as_view(
		template_name='accounts/login.html'), name='login'),
	path('logout/', LogoutView.as_view(
		template_name='accounts/logout.html'), name='logout'),
	path('register/', views.register, name='register'),
	path('profile/', views.user_profile, name='profile'),

	path('create/post/', views.CreatePostView.as_view(template_name='test.html'), name='create'),
	path('update/post/', views.UpdatePostView.as_view(), name='update'),
	path('delete/<int:obj_id>', views.delete_view, name='delete_view'),

	path('posts/', views.ListPostView.as_view(), name='posts'),
	path('posts/<pk>/', views.DetailPostView.as_view(), name='detail'),
]

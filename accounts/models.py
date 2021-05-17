from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile', null=True)
	image = models.ImageField('Avatar', upload_to='user_avatars/', blank=True, null=True)
	address = models.CharField('Address', max_length=150,blank=True)
	brth = models.CharField(max_length=50,blank=True, null=True)


	def get_absolute_url(self):
		pass

	def __str__(self):
		return f"{self.user}"


class TestPost(models.Model):
	title = models.CharField('title', max_length=50)
	body = models.CharField('body', max_length=1050)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('accounts:delete_view', kwargs={'obj_id':self.id})
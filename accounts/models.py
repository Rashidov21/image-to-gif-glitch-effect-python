from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
	image = models.ImageField('Avatar', upload_to='user-avatars/', blank=True, null=True)
	address = models.CharField('Address', max_length=150,blank=True)
	brth = models.DateField(blank=True, null=True)

	def __str__(self):
		return f"{self.user.username}"
from django.contrib import admin
from .models import UserProfile,TestPost
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(TestPost)
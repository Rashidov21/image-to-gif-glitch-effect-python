from django.contrib import admin
from .models import Category, Game, Contact
from django.utils.html import mark_safe

# Register your models here.

admin.site.site_title = "Django GameCenter Project"
admin.site.site_header = "Django GameCenter Project"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','id']
	prepopulated_fields = {'slug':('name',)}
	

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ['title','get_image','category', 'year']
	list_display_links = ['title']
	list_filter = ('year','category', 'budget')

	readonly_fields = ('get_image',)

	def get_image(self, obj):
		return mark_safe(f"<img src='{obj.image.url}' width='100' height='100'>")


	search_fields = ['title', 'info']
	ordering = ['-year']

	prepopulated_fields = {'slug':('title',)}


admin.site.register(Contact)

from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField('Name', max_length=90)
	slug = models.SlugField('*', max_length=90)

	def __str__(self):
		return self.name

class Game(models.Model):
	title = models.CharField('Title', max_length=50)
	slug = models.SlugField('*', max_length=50)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	developer = models.CharField('Developers', max_length=100)
	year = models.DateField('Year',)
	image = models.ImageField('Poster', upload_to='games/')
	budget = models.PositiveIntegerField('Budget', default=0)
	platform = models.CharField('Platform', max_length=100)
	info = models.TextField('Info')

	def __str__(self):
		return self.title 

	class Meta:
		verbose_name_plural = 'Games'



class Contact(models.Model):
	name = models.CharField('Ismi', max_length=50)
	email = models.EmailField('Emaili', max_length=200)
	subject = models.TextField('subject', max_length=150)
	message = models.CharField('Xabari', max_length=50)

	class Meta:
		verbose_name = 'Aloqa'
		verbose_name_plural = 'Aloqalar'

	def __str__(self):
		return f"{self.name}"	
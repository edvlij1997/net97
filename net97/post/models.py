from django.db import models

class PostAdmin(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query) | \
			models.Q(description__icontains=query)
)

class Post(models.Model):
	title = models.CharField('Título', max_length=100)
	link = models.CharField('Link', max_length=200)
	image = models.ImageField('imagem', null=True)

	objects = PostAdmin()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'portfólio'
		verbose_name_plural = 'portfólios'
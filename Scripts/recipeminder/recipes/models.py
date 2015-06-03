from django.db import models

class Recipe(models.Model):

	def __str__(self):
		return self.name
	name = models.CharField(max_length=128)
	created = models.DateTimeField(auto_now_add=True)
	description = models.TextField(null=True)
	servings = models.PositiveIntegerField(null=True)
	ingredients = models.TextField(null=True)
	instructions = models.TextField(null=True)


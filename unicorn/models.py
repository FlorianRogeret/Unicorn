from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
	name = models.Charfield(max_length =150)
	slug = models.SlugField()

class game(models.model):
	name = models.CharField(max_length = 150)
	slug = models.SlugField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	release_date = models.DateTimeField(auto_now_add=True)
	picture = models.ImageField()
	types = models.ManyToManyField(Type)

from django.db import models

# Create your models here.

class family(models.Model):
	persons=models.CharField(max_length=100)
	relation=models.CharField(max_length=100)

	def __str__(self):
		return self. persons
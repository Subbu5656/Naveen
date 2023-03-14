from django.db import models

# Create your models here.

class cinema(models.Model):
	hero=models.CharField(max_length=100)
	vilan=models.CharField(max_length=100)

	def __str__(self):
		return self.hero

 
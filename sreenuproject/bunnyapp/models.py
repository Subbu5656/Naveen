from django.db import models

# Create your models here.

class company(models.Model):
	employe=models.CharField(max_length=100)
	salary=models.CharField(max_length=100)

	def __str__(self):
		return self.employe
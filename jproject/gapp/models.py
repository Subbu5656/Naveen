from django.db import models

# Create your models here.

class carshowroom(models.Model):
	car  = models.CharField(max_length=100)
	model = models.CharField(max_length=100)

	def __str__(self):
		return self.car
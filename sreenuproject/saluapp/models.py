from django.db import models

# Create your models here.

class school(models.Model):
	teacher=models.CharField(max_length=100)
	student=models.CharField(max_length=100)

	def __str__(self):
		return self. teacher

   

    	
	    
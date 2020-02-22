from django.db import models

# Create your models here.
class cmccDemo(models.Model):
	#images
	image = models.ImageField(upload_to = 'imges/')
	#summary
	summary = models.CharField(max_length=200)
from django.db import models

# Create your models here.
class CmccDemo(models.Model):
	#images
	image = models.FileField(upload_to = 'images/')
	#summary
	summary = models.CharField(max_length=200)
	#description
	new_field = models.CharField(max_length=140, default='SOME STRING')


	def __str__(self):
		return self.summary
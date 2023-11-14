from django.db import models

# Create your models here.
class book(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=64)
	year=models.IntegerField()
	price=models.IntegerField()
from django.db import models

# Create your models here.

class Stock(models.Model):
	name = models.CharField(max_length=50)
	info = models.TextField()
	def __str__(self):
		return self.title

class StockHistory(models.Model):
	stock = models.CharField(max_length=50)
	day = models.CharField(max_length=100)
	close = models
	def __str__(self):
		return self.title

class StockIndex(models.Model):
	name = models.CharField(max_length=50)
	stock = models.CharField(max_length=50)

	def __str__(self):
		return self.title

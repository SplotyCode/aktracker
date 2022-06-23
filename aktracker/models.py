from django.db import models

class Stock(models.Model):
	name = models.CharField(max_length=50)
	info = models.TextField()
	def __str__(self):
		return self.name

class StockCloseHistory(models.Model):
	stock = models.CharField(max_length=50)
	day = models.DateField()
	close = models.FloatField()
	def __str__(self):
		return self.stock

class StockIndex(models.Model):
	name = models.CharField(max_length=50)
	stock = models.CharField(max_length=50)

	def __str__(self):
		return self.stock

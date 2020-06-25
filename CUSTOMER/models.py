from django.db import models

# Create your models here.
class Customer(models.Model):
	username = models.CharField(max_length=100)
	jumlah_utang = models.IntegerField()
	#updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.id}. {self.username}'
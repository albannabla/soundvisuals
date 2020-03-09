from django.db import models

class sound(models.Model):
	wavetype = models.CharField('Wave Type', max_length=15)
	frequency = models.IntegerField()


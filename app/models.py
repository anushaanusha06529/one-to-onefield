from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    population = models.BigIntegerField()

class Capital(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.OneToOneField(Country, on_delete=models.CASCADE)    

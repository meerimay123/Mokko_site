from django.db import models

# Create your models here.


class Coffee(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()


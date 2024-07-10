from django.db import models

# Create your models here.


class Coffee(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'Кофе'
        verbose_name = 'Кофе'


class Publication(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    created_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'

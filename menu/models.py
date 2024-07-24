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


class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    comment = models.TextField(max_length=200)
    avatar = models.ImageField()

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'


class MokkoContact(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=155)

    class Meta:
        verbose_name_plural = 'Контакты Мокко'
        verbose_name = 'Контакты Мокко'


class ClientContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    message = models.TextField()

from django.db import models


class Product(models.Model):
    image = models.CharField(max_length=2083)
    videoTime = models.CharField(max_length=50)
    icon = models.CharField(max_length=2083)
    title = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    views = models.FloatField()
    uploadeDay = models.FloatField()


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()



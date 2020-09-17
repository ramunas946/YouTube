from django.db import models
from django.conf import settings


class Product(models.Model):
    image = models.FileField(max_length=2083)
    videoTime = models.CharField(max_length=50)
    icon = models.CharField(max_length=2083)
    title = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    views = models.FloatField()
    uploadeDay = models.FloatField()
    video = models.FileField()
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class UserProfile(models.Model):
    icon = models.FileField()
    user_id = models.IntegerField()
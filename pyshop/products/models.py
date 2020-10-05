from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Product(models.Model):
    image = models.FileField(max_length=2083)
    videoTime = models.CharField(max_length=50)
    icon = models.CharField(max_length=2083)
    title = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    views = models.FloatField()
    uploadeDay = models.FloatField()
    video = models.FileField()
    account = models.ForeignKey(User, on_delete=models.CASCADE)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class UserProfile(models.Model):
    icon = models.ImageField(upload_to="profileicons")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

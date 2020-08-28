from django.db import models
from django.conf import settings

# Create your models here.

class CustomUrl1(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length = 10)
    url = models.CharField(max_length = 200)

class CustomUrl2(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length = 10)
    url = models.CharField(max_length = 200)

class CustomUrl3(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length = 10)
    url = models.CharField(max_length = 200)

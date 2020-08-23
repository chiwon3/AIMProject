from django.db import models
from django.conf import settings

# Create your models here.

class tab11(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    title = models.CharField('구분', blank=False, null=True, max_length=2000)
    result = models.CharField('데이터', blank=False, null=True, max_length=5000)

    def __str__(self):
        return str(self.user)

from django.db import models

# Create your models here.

class NaverWebtoon(models.Model):
    title = models.TextField('타이틀')
    img = models.URLField('썸네일',max_length=2000)
    link = models.URLField('링크',max_length=2000)

    def __str__(self):
        return self.title
from django.db import models


# Create your models here.

class article(models.Model):
    catalog = models.TextField(verbose_name='分裂')
    article_name = models.TextField(verbose_name='文章标题')
    article_url = models.TextField(verbose_name='文章url')
    img_url = models.TextField(verbose_name='文章封面')
    content = models.TextField(verbose_name='文章内容')

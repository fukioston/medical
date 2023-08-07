from django.db import models
from datetime import datetime


# Create your models here.

class articles(models.Model):
    catalog = models.TextField(verbose_name='分裂')
    article_name = models.TextField(verbose_name='文章标题')
    article_url = models.TextField(verbose_name='文章url')
    img_url = models.TextField(verbose_name='文章封面')
    content = models.TextField(verbose_name='文章内容')
    uploader = models.CharField(verbose_name='用户名', max_length=32, default='admin')
    upload_time = models.DateTimeField(verbose_name='上传时间', default=datetime(2023, 8, 7))
    likes = models.IntegerField(verbose_name='点赞数', default=0)
    click = models.IntegerField(verbose_name='点击次数', default=0)

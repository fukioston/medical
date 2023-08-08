from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class articles(models.Model):
    catalog = models.TextField(verbose_name='分类')
    article_name = models.TextField(verbose_name='文章标题')
    article_url = models.TextField(verbose_name='文章url')
    img_url = models.TextField(verbose_name='文章封面')
    content = models.TextField(verbose_name='文章内容')
    uploader_id = models.IntegerField(verbose_name='用户id')
    upload_time = models.TextField(verbose_name='上传日期', default='2023/08/07')
    likes = models.IntegerField(verbose_name='点赞数', default=0)
    click = models.IntegerField(verbose_name='点击量', default=0)
    status=models.CharField(verbose_name='状态', default=0,max_length=32)


class like(models.Model):
    article_id = models.IntegerField(verbose_name='article_id')
    user_id = models.IntegerField(verbose_name='user_id')


class Upload(models.Model):
    """文章模型"""
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )

    title = models.CharField('标题', max_length=200, unique=True)
    body = RichTextUploadingField('正文')

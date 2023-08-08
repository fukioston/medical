from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from datetime import datetime


# Create your models here.

class articles(models.Model):
    """文章模型"""
    CATEGORY_CHOICES = (
        ('居家妙招', '居家妙招'),
        ('饮食妙招', '饮食妙招'),
        ('日常妙招', '日常妙招'),
        ('急救常识', '急救常识'),
        ('灾害急救', '灾害急救'),
        ('意外急救', '意外急救'),
        ('疾病急救', '疾病急救'),
        ('中毒急救', '中毒急救'),
        ('家庭急救', '家庭急救'),
    )
    catalog = models.CharField('分类', max_length=10, choices=CATEGORY_CHOICES)
    article_name = models.CharField('标题', max_length=200, unique=True)
    img_url = models.ImageField('封面', upload_to='static/images/column/articles/')  # 添加封面字段
    content = RichTextUploadingField('正文')
    uploader_id = models.IntegerField(verbose_name='用户id', default=1)
    upload_time = models.TextField(verbose_name='上传日期', default=datetime.now().strftime("%Y/%m/%d"))
    likes = models.IntegerField(verbose_name='点赞数', default=0)
    click = models.IntegerField(verbose_name='点击量', default=0)
    status = models.CharField(verbose_name='状态', default=0, max_length=32)


class like(models.Model):
    article_id = models.IntegerField(verbose_name='article_id')
    user_id = models.IntegerField(verbose_name='user_id')



from django.db import models

# Create your models here.


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号码', max_length=32)
    profile_img= models.CharField(verbose_name='头像', max_length=64, default='doge.jpg')
    identity=models.CharField(verbose_name='身份', max_length=64, default='user')
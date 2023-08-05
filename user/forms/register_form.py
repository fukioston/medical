from django import forms
from user import models
from user.forms.bootstrap import BootStrap
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class RegisterForm(BootStrap,forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['username', 'email', 'password', 'confirm_password', 'mobile_phone', 'code']


    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request


# 手机号
    mobile_phone = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式不正确'), ]
)
    # email = forms.CharField(
    #     label='邮箱',
    #     validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '邮箱格式不正确'), ]
    # )

    password = forms.CharField(
        label='密码',
    # widget=forms.PasswordInput(attrs={'class': 'form-control'})
        widget=forms.PasswordInput(),
        min_length=6,
        max_length=20,
        error_messages={
            'min_length': "密码不能小于6个字符",
            'max_length': "密码不能大于20个字符"

    }
)

    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(),
        min_length=6,
        max_length=20,
        error_messages={
            'min_length': "重复密码⻓度不能⼩于6个字符",
            'max_length': "重复密码⻓度不能⼤于20个字符"
    },
)

    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput()
)
    def clean_username(self):
        username = self.cleaned_data['username']
        exists = models.UserInfo.objects.filter(username=username).exists()
        if exists:
            raise ValidationError('⽤户名已存在')
            # self.add_error('username','⽤户名已存在')
        return username
    def clean_email(self):
        username = self.cleaned_data['email']
        exists = models.UserInfo.objects.filter(username=username).exists()
        if exists:
            raise ValidationError('邮箱已存在')
            # self.add_error('username','⽤户名已存在')
        return username

    def clean_password(self):
        pwd = self.cleaned_data['password']
        return pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm_pwd = self.cleaned_data['confirm_password']
        if pwd != confirm_pwd:
            raise ValidationError('两次密码不⼀致')
        return confirm_pwd
    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        exists = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
        if exists:
            raise ValidationError('电话已存在')
        return mobile_phone
    def clean_code(self):
        code = self.cleaned_data['code']
        mobile_phone = self.cleaned_data.get('mobile_phone')
        if not mobile_phone :
            return code
        redis_code = self.request.session.get('code')  # 从session中获取验 证码
        if not redis_code:
            raise ValidationError('验证码失效或未发送，请重新发送')
        # redis_str_code = redis_code.decode('utf-8')
        # if code.strip() != redis_code:
        if code != redis_code:
            raise ValidationError('验证码错误，请重新输⼊')
        return code

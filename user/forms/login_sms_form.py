from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django.http import HttpResponse
from jsonschema.exceptions import ValidationError

from user import models
from utils.tencent.sms import send_sms_single
import random
from user.forms.bootstrap import BootStrap


class LoginSmsForm(BootStrap, forms.Form):
    mobile_phone = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式不正确'), ]
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput())

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    #     未进行检验
    # def clean_mobile_phone(self):
    #     mobile_phone = self.cleaned_data['mobile_phone']
    #     exists = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
    #
    #     if not exists:
    #         raise ValidationError('⼿机号不存在')
    #     return mobile_phone
    # #
    def clean_code(self):
        code = self.cleaned_data['code']
        print(code)
        mobile_phone = self.cleaned_data.get('mobile_phone')
        # ⼿机号不存在，则验证码⽆需再校验
        if not mobile_phone:
            return code
        session_code = self.request.session.get('code')  # 从session中获取验证码
        if not session_code:
            raise ValidationError('验证码失效或未发送，请重新发送')
        # redis_str_code = redis_code.decode('utf-8')
        if code.strip().upper() != session_code.strip().upper():
            raise ValidationError('验证码错误，请重新输⼊')
        return code

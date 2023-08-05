from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from django.conf import settings
from django.http import HttpResponse

from user import models
from utils.tencent.sms import send_sms_single
import random


class SendSmsForm(forms.Form):
    # 这个是发送短信的表单
    # 重写__init__函数,加个request
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    mobile_phone = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式不正确'), ]
    )
    # 已经进行检验
    def clean_mobile_phone(self):
        # 从表单中取出mobile_phone
        mobile_phone = self.cleaned_data['mobile_phone']
        print(mobile_phone)
        tpl = self.request.GET.get('tpl')
        template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
        if not template_id:
            return ValidationError('模版不存在')
        exists = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
        if tpl == 'login':
            if not exists:
                print("??1")
                raise ValidationError('手机号不存在')
        else:
            if exists:
                print("??2")
                raise ValidationError('手机号已存在')
        # 生成验证码
        code = random.randrange(1000, 9999)
        print("验证码：" + str(code))
        response = send_sms_single(mobile_phone, template_id, [code, 5])
        self.request.session['code'] = str(code)
        self.request.session.set_expiry(300)
        return mobile_phone
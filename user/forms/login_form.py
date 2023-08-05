from django import forms
from django.core.validators import RegexValidator
from hashlib import md5
from jsonschema.exceptions import ValidationError

from user import models
from user.forms.bootstrap import BootStrap


class LoginForm(BootStrap, forms.Form):
    mobile_phone = forms.CharField(
        label='手机号',
        widget=forms.TextInput(),
        required=True,
        validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式不正确'), ]
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(render_value=True),
        required=True
    )
    code = forms.CharField(label='图⽚验证码')
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # def clean_password(self):
    #     pw = self.cleaned_data.get('password')
    #     return md5(pw.encode()).hexdigest()

    def clean_code(self):
        """ 钩⼦ 图⽚验证码是否正确？ """
        # 读取⽤户输⼊的验证码
        code = self.cleaned_data['code']
        # 去session获取⾃⼰的验证码
        session_code = self.request.session.get('image_code')
        if not session_code:
            raise ValidationError('验证码已过期，请重新获取')
        if code.strip().upper() != session_code.strip().upper():
            raise ValidationError('验证码输⼊错误')
        return code
from django import forms
from django.core.validators import RegexValidator
from hashlib import md5
from jsonschema.exceptions import ValidationError

from user import models
from user.forms.bootstrap import BootStrap


class InfoForm(BootStrap, forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(),
        required=True,
    )
    mobile_phone = forms.CharField(
        label='手机号',
        widget=forms.TextInput,
        required=True,
    )
    email = forms.CharField(
        label='邮箱',
        widget=forms.TextInput(),
        required=True,
    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request


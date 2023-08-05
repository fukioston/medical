from django import forms
from django.core.validators import RegexValidator
from hashlib import md5
from jsonschema.exceptions import ValidationError

from user import models
from user.forms.bootstrap import BootStrap


class PwdForm(BootStrap, forms.Form):
    old_pwd=forms.CharField(
        label='旧密码',
        widget=forms.PasswordInput(render_value=True),
        required=True)
    new_pwd = forms.CharField(
        label='新密码',
        widget=forms.PasswordInput(render_value=True),
        required=True)


    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request


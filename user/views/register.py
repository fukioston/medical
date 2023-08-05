from django.http import JsonResponse
from django.shortcuts import render, redirect
from jsonschema.exceptions import ValidationError

from user.forms.register_form import RegisterForm


def register(request):
    if request.method == 'GET':
        form = RegisterForm(request)
        return render(request, 'user/register.html', {'form': form})
    else:
        form = RegisterForm(request, data=request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('/user/login/sms/')
            form.add_error('mobile_phone', '手机号或验证码错误')
        except ValidationError as e:
            form.add_error('code', e)
        return render(request, 'user/register.html', {'form': form})
    # try:
    #     if form.is_valid():
    #         mobile_phone = form.cleaned_data['mobile_phone']
    #         user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
    #         if user_object:
    #             request.session['id'] = user_object.id
    #             request.session['username'] = user_object.username
    #             request.session.set_expiry(60 * 60 * 24 * 14)
    #             return redirect('/user/index/')
    #         form.add_error('mobile_phone', '手机号或验证码错误')
    # except ValidationError as e:
    #     form.add_error('code', e)
    # return render(request, 'user/login_sms.html', {'form': form})
from io import BytesIO

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from jsonschema.exceptions import ValidationError
from user.forms.login_form import LoginForm
from user import models
from user.forms.login_sms_form import LoginSmsForm
from user.forms.register_form import RegisterForm
from user.forms.send_sms_form import SendSmsForm
from user.models import UserInfo
from utils.image_code import check_code


def login(request):
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'user/login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    try:
        if form.is_valid():
            mobile_phone = form.cleaned_data['mobile_phone']
            password = form.cleaned_data['password']
            user = UserInfo.objects.get(mobile_phone=mobile_phone)
            if user.password == password:
                # 登录成功，将用户标识存储在session中
                request.session["info"] = {'id': user.id, 'name': user.username}
                request.session.set_expiry(60 * 60 * 24 * 14)
                return redirect('/column/catalog')  # 重定向到登录成功后的页面
            else:
                form.add_error('password', '密码错误!')
    except ValidationError as e:
        form.add_error('code', e)
    return render(request, 'user/login.html', {'form': form})


def send_sms(request):
    form = SendSmsForm(request, data=request.GET)
    if form.is_valid():
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})


def login_sms(request):
    if request.method == 'GET':
        form = LoginSmsForm(request)

        return render(request, 'user/login_sms.html',{'form':form})

    form = LoginSmsForm(request, data=request.POST)
    try:
        if form.is_valid():
            mobile_phone = form.cleaned_data['mobile_phone']
            user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
            if user_object:
                request.session['id'] = user_object.id
                request.session['username'] = user_object.username
                request.session.set_expiry(60 * 60 * 24 * 14)
                return redirect('/column/catalog')
            form.add_error('mobile_phone', '手机号或验证码错误')
    except ValidationError as e:
        form.add_error('code', e)
    return render(request, 'user/login_sms.html', {'form': form})
def image_code(request):
    # 生成图片验证码
    image_object, code = check_code()
    request.session['image_code'] = code
    request.session.set_expiry(6000)  # 主动修改验证码的过期时间为60s
    # 将图⽚信息保存到内存中使⽤省去每次都去数据库查询的操作
    stream = BytesIO()
    image_object.save(stream, 'png')
    return HttpResponse(stream.getvalue())






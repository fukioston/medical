from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from user.forms.edit_info import InfoForm
from user.forms.edit_pwd import PwdForm
from user.models import UserInfo
import os

def home(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    # on_sales_num = Items.objects.filter(userid=user_id).count()

    return render(request, 'user/home.html', {'user_info': query_set,})





def logout(request):
    request.session.flush()
    return redirect('/item/')

def edit_info(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    if request.method == 'GET':
        user_info = UserInfo.objects.filter(id=user_id).values_list('username', 'email', 'mobile_phone','profile_img').first()
        init_info = {'username': user_info[0], 'mobile_phone': user_info[2], 'email': user_info[1]}
        form = InfoForm(request, initial=init_info)
        return render(request, 'user/edit_info.html', {'user_info': query_set, 'form': form})

    form = InfoForm(request, data=request.POST)
    user = UserInfo.objects.filter(id=user_id).first()
    if form.is_valid():
        file = request.FILES.get('file')
        if file:
            newimg = file.name
            user.profile_img=newimg
            with open(os.path.join('static/profile_img', file.name), 'wb') as f:  # 在static目录下创建同名文件
                for line in file.chunks():
                    f.write(line)
        new_name = form.cleaned_data['username']
        new_phone = form.cleaned_data['mobile_phone']
        new_email = form.cleaned_data['email']
        user.username = new_name
        user.mobile_phone = new_phone
        user.email = new_email
        user.save()
        print('info_saved!')
        return redirect('/user/home/')


def edit_pwd(request):
    info = request.session.get('info')
    user_id = info['id']
    print(user_id)
    query_set = UserInfo.objects.filter(id=user_id).first()
    print(query_set)
    if request.method == 'GET':
        user_info = UserInfo.objects.filter(id=user_id).values_list('username', 'email', 'mobile_phone').first()

        form = PwdForm(request)
        return render(request, 'user/edit_pwd.html', {'form': form,'user_info':query_set})

    form = PwdForm(request, data=request.POST)
    user = UserInfo.objects.filter(id=user_id).first()
    if form.is_valid():
        old_pwd = form.cleaned_data['old_pwd']
        new_pwd = form.cleaned_data['new_pwd']
        if old_pwd==user.password:
            if old_pwd==new_pwd:
                form.add_error('new_pwd', '新密码不能与旧密码相同')
                return render(request, 'user/edit_pwd.html', {'form': form})
            user.password=new_pwd
            return redirect('/user/home/')
        else:
            form.add_error('old_pwd', '旧密码错误')
            return render(request, 'user/edit_pwd.html', {'form': form})
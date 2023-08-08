from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from user.models import UserInfo
from column.forms.article_form import UploadForm


def upload(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    if request.method == 'GET':
        form = UploadForm
        return render(request, 'column/upload.html', {'form': form, 'user_info': query_set})
    else:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.uploader_id = user_id
            form.instance.status = 1
            form.save()
            return redirect('catalog.home')
        else:
            print(form.errors)  # 打印验证错误信息

        return HttpResponse('提交失败！')


from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from user.models import UserInfo
from column.forms.article_form import UploadForm
from column.models import articles

import time


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
            form.instance.status = 0
            form.save()
            return redirect('catalog.home')
        else:
            print(form.errors)  # 打印验证错误信息

        return HttpResponse('提交失败！')


def edit_article(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    article_name = request.GET.get('article_name')
    article = articles.objects.filter(article_name=article_name).first()

    if request.method == 'POST':
        form = UploadForm(request.POST, instance=article)
        if form.is_valid():
            # 修改后要重新审核
            form.instance.status = 0
            form.save()
            time.sleep(10)
            return redirect('/column/catalog', {'user_info': query_set})
    else:
        form = UploadForm(instance=article)

    return render(request, 'column/edit_article.html', {'user_info': query_set, 'form': form})


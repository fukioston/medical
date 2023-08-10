from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from column.models import articles
from user.models import UserInfo, like


def article(request):
    article_name = request.GET.get('article_name')
    if article_name:
        articles_obj = articles.objects.filter(article_name=article_name).first()
        if articles_obj:
            articles_obj.click += 1
            articles_obj.save()
            print(articles_obj.click)
    else:
        articles_obj = None

    article_content = articles_obj.content
    article_id = articles_obj.id
    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'column/article.html',
                      {'article_id': article_id, 'title': article_name, 'content': article_content,
                       'user_info': query_set})
    return render(request, 'column/article.html',
                  {'article_id': article_id, 'title': article_name, 'content': article_content})


def show_collects(request):
    uinfo = request.session.get('info')
    user_id = uinfo['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    article_ids = like.objects.filter(user_id=user_id)
    article_objs = []
    for article_id in article_ids:
        article_objs.append(articles.objects.filter(id=article_id.article_id, status=1).first())
    articles_id = [article_obj.id for article_obj in article_objs]
    article_name_list = [article_obj.article_name for article_obj in article_objs]
    article_img_list = [article_obj.img_url for article_obj in article_objs]
    for i in range(len(article_img_list)):
        s = str(article_img_list[i])
        if s.__contains__('static'):
            article_img_list[i] = '/' + s
            print(article_img_list[i])

    article_uploader_img = [UserInfo.objects.filter(id=article_obj.uploader_id).first().profile_img
                            for article_obj in article_objs]
    article_uploader = [UserInfo.objects.filter(id=article_obj.uploader_id).first().username
                        for article_obj in article_objs]
    article_upload_time = [article_obj.upload_time for article_obj in article_objs]
    article_likes = [article_obj.likes for article_obj in article_objs]
    article_click = [article_obj.click for article_obj in article_objs]
    info = list(
        zip(article_name_list, article_img_list, article_uploader, article_upload_time, article_likes, article_click,
            articles_id, article_uploader_img))

    return render(request, 'column/collects.html', {'info_list': info, 'user_info': query_set})


def iscollect(request):
    uinfo = request.session.get('info')
    if uinfo:
        user_id = uinfo['id']
        article_id = request.GET.get('article_id')
        try:
            if like.objects.get(user_id=user_id, article_id=article_id):
                print('sss')
                return JsonResponse({'status': True, 'err': "已经收藏"})
        except like.DoesNotExist:
            # 如果表中没有数据
            return JsonResponse({'status': False})
    redirect('user/login')

def change_favorite(request):
    uinfo = request.session.get('info')
    if uinfo:
        user_id = uinfo['id']
        article_id = request.POST.get('article_id')
        try:
            if like.objects.get(user_id=user_id, article_id=article_id):
                return JsonResponse({'status': False, 'err': "已经收藏"})
        except like.DoesNotExist:
            like.objects.create(user_id=user_id, article_id=article_id)
            # 如果表中没有数据
            return JsonResponse({'status': True})
    redirect('user/login')

def cancel_favorite(request):
    uinfo = request.session.get('info')
    if uinfo:
        user_id = uinfo['id']
        article_id = request.POST.get('article_id')
        if like.objects.get(user_id=user_id, article_id=article_id):
            like.objects.filter(user_id=user_id, article_id=article_id).delete()
            return JsonResponse({'status': True, 'err': "已经取消收藏"})
    redirect('user/login')

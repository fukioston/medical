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
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'column/article.html', {'article_id':article_id,'title': article_name, 'content': article_content, 'user_info': query_set})


def iscollect(request):
    user_id=request.GET.get('user_id')
    article_id=request.GET.get('article_id')
    print(user_id+'aaaa'+article_id)
    try:
        if like.objects.get(user_id=user_id,article_id=article_id):
            print('sss')
            return JsonResponse({'status': True, 'err': "已经收藏"})
    except like.DoesNotExist:
        # 如果表中没有数据
        return JsonResponse({'status': False})


def change_favorite(request):
    article_id= request.POST.get('article_id')
    user_id = request.POST.get('user_id')
    print(article_id)
    print(user_id)
    # 如果表中有了数据就报错
    try:
        if like.objects.get(user_id=user_id,article_id=article_id):
            return JsonResponse({'status': False, 'err': "已经收藏"})
    except like.DoesNotExist:
        like.objects.create(user_id=user_id,article_id=article_id)
        # 如果表中没有数据
        return JsonResponse({'status': True})


def cancel_favorite(request):
    article_id = request.POST.get('article_id')
    user_id = request.POST.get('user_id')
    print(article_id)
    print(user_id)
    if like.objects.get(user_id=user_id,article_id=article_id):
        like.objects.filter(user_id=user_id,article_id=article_id).delete()
        return JsonResponse({'status': True, 'err': "已经取消收藏"})
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from column.models import articles
from user.models import UserInfo


def home(request):
    counts = []
    catalog_list = articles.objects.values_list('catalog', flat=True).distinct()
    for catalog in catalog_list:
        counts.append([catalog, articles.objects.filter(catalog=catalog).count()])
    print(counts)
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'column/catalog.html', {'class': counts,'user_info':query_set,})


def article_list(request):
    catalog = request.GET.get('catalog')  # 获取参数值
    print(catalog)
    if catalog:
        articles_obj = articles.objects.filter(catalog=catalog)
    else:
        articles_obj = None
    articles_id=[article_obj.id for article_obj in articles_obj]
    article_name_list = [article_obj.article_name for article_obj in articles_obj]
    article_img_list = [article_obj.img_url for article_obj in articles_obj]
    article_uploader_img = [UserInfo.objects.filter(id=article_obj.uploader_id).first().profile_img
                        for article_obj in articles_obj]
    article_uploader = [UserInfo.objects.filter(id=article_obj.uploader_id ).first().username
                        for article_obj in articles_obj]
    article_upload_time = [article_obj.upload_time for article_obj in articles_obj]
    article_likes = [article_obj.likes for article_obj in articles_obj]
    article_click = [article_obj.click for article_obj in articles_obj]
    info = list(zip(article_name_list, article_img_list, article_uploader, article_upload_time, article_likes, article_click,articles_id,article_uploader_img))
    uinfo = request.session.get('info')
    user_id = uinfo['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'column/article_list.html', {'info_list': info,'user_info':query_set})

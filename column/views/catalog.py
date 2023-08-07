from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from column.models import articles


def home(request):
    counts = []
    catalog_list = articles.objects.values_list('catalog', flat=True).distinct()
    for catalog in catalog_list:
        counts.append([catalog, articles.objects.filter(catalog=catalog).count()])
    print(counts)
    return render(request, 'column/catalog.html', {'class': counts})


def article_list(request):
    catalog = request.GET.get('catalog')  # 获取参数值
    print(catalog)
    if catalog:
        articles_obj = articles.objects.filter(catalog=catalog)
    else:
        articles_obj = None

    article_name_list = [article_obj.article_name for article_obj in articles_obj]
    article_img_list = [article_obj.img_url for article_obj in articles_obj]
    article_uploader = [article_obj.uploader for article_obj in articles_obj]
    article_upload_time = [article_obj.upload_time for article_obj in articles_obj]
    article_likes = [article_obj.likes for article_obj in articles_obj]
    article_click = [article_obj.click for article_obj in articles_obj]
    info = list(zip(article_name_list, article_img_list, article_uploader, article_upload_time, article_likes, article_click))

    return render(request, 'column/article_list.html', {'info_list': info})

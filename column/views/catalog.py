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
    info = list(zip(article_name_list, article_img_list))
    return render(request, 'column/article_list.html', {'info_list': info})

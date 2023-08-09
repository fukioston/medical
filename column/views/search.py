from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from column.models import articles


def search(request):
    return render(request, 'column/search.html', )


def search_tip(request):
    kw = request.POST.get('kw')
    article_objs = articles.objects.filter(article_name__contains=kw)
    article_name_list = [article_obj.article_name.strip().lower() for article_obj in article_objs]
    article_name_list = list(set(article_name_list))
    if len(article_name_list) > 5:
        article_name_list = []
    print(article_name_list)

    return JsonResponse({'status': True, 'err': "无法回复", 'info': article_name_list})

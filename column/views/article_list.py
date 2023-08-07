from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from column.models import articles


def article(request):
    article_name = request.GET.get('article_name')
    if article_name:
        articles_obj = articlesm.objects.filter(article_name=article_name)
    else:
        articles_obj = None

    article_title = [article_obj.article_name for article_obj in articles_obj]
    article_content = [article_obj.content for article_obj in articles_obj]
    info = list(zip(article_title, article_content))
    return render(request, 'column/article.html', {'info': info})

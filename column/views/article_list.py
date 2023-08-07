from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from column.models import articles


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
    print(article_name)
    print(article_content)
    return render(request, 'column/article.html', {'title': article_name, 'content': article_content})

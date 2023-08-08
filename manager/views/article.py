from django.shortcuts import render

from column.models import articles
from user.models import UserInfo


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
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'manager/article.html', {'title': article_name, 'content': article_content, 'user_info': query_set})
from django.http import JsonResponse
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
    else:
        articles_obj = None

    article_content = articles_obj.content
    article_id = articles_obj.id
    article_status=articles_obj.status
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'manager/article.html', {'article_status':article_status,'article_id':article_id,'title': article_name, 'content': article_content, 'user_info': query_set})


def agreed(request):
    id=request.POST.get('id')
    article_obj = articles.objects.filter(id=id).first()
    article_obj.status="1"
    article_obj.save()
    return JsonResponse({'status': True,  })


def notagreed(request):
    id = request.POST.get('id')
    article_obj = articles.objects.filter(id=id).first()
    article_obj.status = "2"
    article_obj.save()
    return JsonResponse({'status': True,  })
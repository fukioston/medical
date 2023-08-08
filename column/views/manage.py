from django.http import JsonResponse
from django.shortcuts import render, redirect,HttpResponse

from column.models import articles
from user.models import UserInfo
def mymanage(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'column/manage.html', {'user_info': query_set, })


def get_all(request):
    articles_obj = articles.objects.filter().order_by('upload_time')
    articles_id = [article_obj.id for article_obj in articles_obj]
    article_name_list = [article_obj.article_name for article_obj in articles_obj]
    article_uploader = [UserInfo.objects.filter(id=article_obj.uploader_id).first().username
                        for article_obj in articles_obj]
    article_upload_time = [article_obj.upload_time for article_obj in articles_obj]
    article_catalog = [article_obj.catalog for article_obj in articles_obj]
    article_status = [article_obj.status  for article_obj in articles_obj]
    info = list(
        zip( articles_id,article_name_list, article_catalog, article_status,article_upload_time,article_uploader, ))
    return JsonResponse({'status': True, 'err': "无法回复", 'info':info})
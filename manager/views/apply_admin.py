from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

from column.models import articles
from user.models import UserInfo
@csrf_exempt

def apply_admin(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'manager/apply_admin.html', {'user_info':query_set, })


def satisfy(request):
    info = request.session.get('info')
    user_id = info['id']
    condition1 = False
    condition2 = False
    condition3 = False
    query_set = UserInfo.objects.filter(id=user_id).first()
    # 条件一满足
    if query_set.identity == 'user':
        condition1 = True
    # 条件二满足
    articles_obj = articles.objects.filter(uploader_id=user_id)
    count = articles_obj.count()
    if count >= 10:
        condition2 = True
    count2 = articles_obj.aggregate(Sum('click'))['click__sum']
    if count2 > 1:
        condition3 = True
    condition = []
    condition.append(condition1)
    condition.append(condition2)
    condition.append(condition3)

    return JsonResponse({'status': True, 'condition': condition, })


def apply(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    query_set.identity='admin'
    query_set.save()
    return JsonResponse({'status': True,  })


from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from column.models import articles
from user.models import UserInfo


def search(request):
    return render(request, 'column/search.html', )


def search_tip(request):
    info=2
    return JsonResponse({'status':True, 'err': "无法回复",'info':info})

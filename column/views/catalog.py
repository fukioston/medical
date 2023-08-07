from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


def home(request):
    return render(request, 'column/catalog.html')


def article_list(request):
    catalog = request.GET.get('catalog')  # 获取参数值
    print(catalog)

    return render(request, 'column/article_list.html')

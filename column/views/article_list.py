from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


def article(request):

    return render(request, 'column/article.html')


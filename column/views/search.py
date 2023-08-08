from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from column.models import articles
from user.models import UserInfo
def search(request):
    return render(request, 'column/search.html',)
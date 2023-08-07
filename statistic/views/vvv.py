from django.http import JsonResponse
from django.shortcuts import render, redirect

def statistic(request):
    return render(request, 'statistic/sta.html')
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


def home(request):

    return render(request, 'column/catalog.html')
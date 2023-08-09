from django.shortcuts import render


def home(request):
    return render(request,'medicine_info/home.html')
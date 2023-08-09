from django.shortcuts import render


def home(request):
    return render(request, 'medical_info/home.html')
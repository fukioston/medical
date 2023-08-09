from django.shortcuts import render

def search(request):
    return render(request, 'medical_info/search.html')
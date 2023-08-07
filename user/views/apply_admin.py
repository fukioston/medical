from django.shortcuts import render, HttpResponse, redirect
def apply_admin(request):
    return render(request,'user/apply_admin.html')
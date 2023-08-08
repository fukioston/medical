"""medical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from manager.views import apply_admin, manage

urlpatterns = [
    path('apply_admin', apply_admin.apply_admin),
    path('satisfy', apply_admin.satisfy),
    path('apply', apply_admin.apply),
    path('manage', manage.mymanage),
    path('manage/review',manage.review),
    path('get_all', manage.get_all),
    path('get_reviewing',manage.get_reviewing)
]

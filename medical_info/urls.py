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

from medical_info.views import home, info, search, detail_info

urlpatterns = [
    path('home',home.home),
    path('search', search.search),
    path('symptom_info',info.symptom_info),
    path('get_symptom_info',info.get_symptom_info),
    path('get_select_symptom',info.get_select_symptom),
    path('get_department',info.get_department),
    path('disease_info', info.disease_info),
    path('get_disease_info', info.get_disease_info),
    path('get_department2',info.get_department2),
    path('get_select_disease', info.get_select_disease),
    path('diagnose_info', info.diagnose_info),
    path('get_diagnose_info', info.get_diagnose_info),
    path('get_select_diagnose', info.get_select_diagnose),
    path('get_department3',info.get_department3),
    path('drug_info', info.drug_info),
    path('get_drug_info', info.get_drug_info),
    path('detail/<item>', detail_info.drug_detail),


]

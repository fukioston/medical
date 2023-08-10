from django.http import JsonResponse
from django.shortcuts import render
from medical.settings import g
import json

from user.models import UserInfo


def drug_detail(request):
    item = request.GET.get('item')
    print(item)
    query = (
            "MATCH (n:Drug {name:\"" + item + "\"})  RETURN n"
    )
    answer = g.run(query).data()
    json_data = []
    print(answer)
    for record in answer:
        print(record)
        data = {
            'n': record['n'],
        }
        json_data.append(data)

    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'medical_info/home.html', {'user_info': query_set, 'data': json_data})
    else:
        return render(request, 'medical_info/drug_detail_info.html', {'data': json_data})


def symptom_detail(request):
    item = request.GET.get('item')
    print(item)
    query = (
            "MATCH (n:Symptom {name:\"" + item + "\"})  RETURN n"
    )
    answer = g.run(query).data()
    json_data = []
    print(answer)
    for record in answer:
        print(record)
        data = {
            'n': record['n'],
        }
        json_data.append(data)
    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'medical_info/symptom_detail.html', {'data': json_data, 'user_info': query_set})
    else:
        return render(request, 'medical_info/symptom_detail.html', {'data': json_data})


def disease_detail(request):
    disease = request.GET.get('disease')
    query = (
            "MATCH (n:Disease {name:\"" + disease + "\"})  RETURN n"
    )
    answer = g.run(query).data()
    json_data = []
    print(answer)
    for record in answer:
        print(record)
        data = {
            'n': record['n'],
        }
        json_data.append(data)
    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'medical_info/disease_detail.html', {'data': json_data, 'user_info': query_set})
    return render(request, 'medical_info/disease_detail.html', {'data': json_data})


def check_detail(request):
    check = request.GET.get('check')
    query = (
            "MATCH (n:Check {name:\"" + check + "\"})  RETURN n"
    )
    answer = g.run(query).data()
    json_data = []
    print(answer)
    for record in answer:
        print(record)
        data = {
            'n': record['n'],
        }
        json_data.append(data)
    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'medical_info/diagnose_detail.html', {'data': json_data, 'user_info': query_set})
    else:
        return render(request, 'medical_info/diagnose_detail.html', {'data': json_data})

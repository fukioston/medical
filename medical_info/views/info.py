from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from medical.settings import g
from user.models import UserInfo


def symptom_info(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    if query_set:
        return render(request, 'medical_info/symptom_info.html', {'user_info': query_set})
    else:
        return render(request, 'medical_info/symptom_info.html', )


def get_symptom_info(request):
    page = request.GET.get('page')
    page = int(page)
    print(page)
    query = (
        "MATCH (n:Symptom)-[r:BELONGS_TO]->(p:Department) "  # 假设 n 和 p 之间有某种关系，修改为实际关系
        "RETURN ID(n) AS id,n,  p.name AS department_name "  # 选择需要的属性
    )
    answer = g.run(
        query).data()
    json_data = []
    for record in answer:
        data = {
            'n': record['n'],
            'id': record['id'],
            'department_name': record['department_name']
        }
        json_data.append(data)
    # 返回JSON响应
    json_data = json_data[(page - 1) * 10:page * 10]
    return JsonResponse(json_data, safe=False)


def get_select_symptom(request):
    page = request.GET.get('page')
    page = int(page)
    department = request.GET.get('department')
    print(department)
    answer = g.run(
        "MATCH (n:Symptom)-[r:BELONGS_TO]->(p:Department{name:\"" + department + "\"}) RETURN ID(n) AS id,n ").data()
    json_data = []
    for record in answer:
        data = {
            'n': record['n'],
            'id': record['id'],
        }
        json_data.append(data)
    json_data = json_data[(page - 1) * 10:page * 10]
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)


def get_department(request):
    answer = g.run(
        "MATCH (n:Symptom)-[r:BELONGS_TO]->(p:Department) RETURN distinct p ").data()
    json_data = []
    for record in answer:
        json_data.append(record['p'])
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)


def disease_info(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    if query_set:
        return render(request, 'medical_info/disease_info.html', {'user_info': query_set})
    else:
        return render(request, 'medical_info/disease_info.html')


def get_disease_info(request):
    page = request.GET.get('page')
    page = int(page)
    print(page)
    query = (
        "MATCH (n:Disease)-[r:BELONGS_TO]->(p:Department) "  # 假设 n 和 p 之间有某种关系，修改为实际关系
        "RETURN ID(n) AS id,n,  p.name AS department_name "  # 选择需要的属性
    )
    answer = g.run(
        query).data()
    json_data = []
    for record in answer:
        data = {
            'n': record['n'],
            'id': record['id'],
            'department_name': record['department_name']
        }
        json_data.append(data)
    # 返回JSON响应
    json_data = json_data[(page - 1) * 10:page * 10]
    return JsonResponse(json_data, safe=False)


def get_select_disease(request):
    page = request.GET.get('page')
    page = int(page)
    department = request.GET.get('department')
    print(department)
    answer = g.run(
        "MATCH (n:Disease)-[r:BELONGS_TO]->(p:Department{name:\"" + department + "\"}) RETURN ID(n) AS id,n ").data()
    json_data = []
    for record in answer:
        data = {
            'n': record['n'],
            'id': record['id'],
        }
        json_data.append(data)
    json_data = json_data[(page - 1) * 10:page * 10]
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)


def get_department2(request):
    answer = g.run(
        "MATCH (n:Disease)-[r:BELONGS_TO]->(p:Department) RETURN distinct p ").data()
    json_data = []
    for record in answer:
        json_data.append(record['p'])
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)


def diagnose_info(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    if query_set:
        return render(request, 'medical_info/diagnose_info.html', {'user_info': query_set})
    else:
        return render(request, 'medical_info/diagnose_info.html')


def get_diagnose_info(request):
    page = request.GET.get('page')
    page = int(page)
    print(page)
    query = (
        "MATCH (n:Check)-[r:BELONGS_TO]->(p:Department) "  # 假设 n 和 p 之间有某种关系，修改为实际关系
        "RETURN ID(n) AS id,n,  p.name AS department_name "  # 选择需要的属性
    )
    answer = g.run(
        query).data()
    json_data = []
    for record in answer:
        data = {
            'n': record['n'],
            'id': record['id'],
            'department_name': record['department_name']
        }
        json_data.append(data)
    # 返回JSON响应
    json_data = json_data[(page - 1) * 10:page * 10]
    return JsonResponse(json_data, safe=False)


def get_select_diagnose(request):
    page = request.GET.get('page')
    page = int(page)
    department = request.GET.get('department')
    print(department)
    answer = g.run(
        "MATCH (n:Check)-[r:BELONGS_TO]->(p:Department{name:\"" + department + "\"}) RETURN ID(n) AS id,n ").data()
    json_data = []
    for record in answer:
        data = {
            'n': record['n'],
            'id': record['id'],
        }
        json_data.append(data)
    json_data = json_data[(page - 1) * 10:page * 10]
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)


def get_department3(request):
    answer = g.run(
        "MATCH (n:Check)-[r:BELONGS_TO]->(p:Department) RETURN distinct p ").data()
    json_data = []
    for record in answer:
        json_data.append(record['p'])
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)


def drug_info(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    if query_set:
        return render(request, 'medical_info/drug_info.html', {'user_info': query_set})
    else:
        return render(request, 'medical_info/drug_info.html')


def get_drug_info(request):
    page = request.GET.get('page')
    page = int(page)
    print(page)
    query = (
        "MATCH (n:Disease)-[r:RECOMMAND_DRUG]->(d:Drug) "  # 假设 n 和 p 之间有某种关系，修改为实际关系
        "RETURN ID(d) AS id, d,  n.name AS disease_name "  # 选择需要的属性
    )
    answer = g.run(
        query).data()
    json_data = []
    for record in answer:
        data = {
            'd': record['d'],
            'id': record['id'],
            'disease_name': record['disease_name']
        }
        json_data.append(data)
    # 返回JSON响应
    json_data = json_data[(page - 1) * 10:page * 10]
    return JsonResponse(json_data, safe=False)

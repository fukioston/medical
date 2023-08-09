from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from medical.settings import g


def symptom_info(request):
    return render(request, 'medical_info/symptom_info.html')


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
            'id':record['id'],
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
    return render(request, 'medical_info/disease_info.html')


def get_disease_info(request):
    page = request.GET.get('page')
    page = int(page)
    answer = g.run(
        "MATCH (n:Disease) RETURN n").data()
    json_data = []
    for record in answer:
        json_data.append(record['n'])
    # 返回JSON响应
    json_data = json_data[(page - 1) * 10:page * 10]
    return JsonResponse(json_data, safe=False)


def get_select_disease(request):
    page = request.GET.get('page')
    page = int(page)
    department = request.GET.get('department')
    print(department)
    answer = g.run(
        "MATCH (n:Disease)-[r:BELONGS_TO]->(p:Department{name:\"" + department + "\"}) RETURN n ").data()
    json_data = []
    for record in answer:
        json_data.append(record['n'])
    json_data = json_data[(page - 1) * 10:page * 10]
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)


def diagnose_info(request):
    return render(request, 'medical_info/diagnose_info.html')


def get_diagnose_info(request):
    page = request.GET.get('page')
    page = int(page)
    answer = g.run(
        "MATCH (n:Check) RETURN n").data()
    json_data = []
    for record in answer:
        json_data.append(record['n'])
    # 返回JSON响应
    json_data = json_data[(page - 1) * 10:page * 10]
    return JsonResponse(json_data, safe=False)


def get_select_diagnose(request):
    page = request.GET.get('page')
    page = int(page)
    department = request.GET.get('department')
    print(department)
    answer = g.run(
        "MATCH (n:Check)-[r:BELONGS_TO]->(p:Department{name:\"" + department + "\"}) RETURN n ").data()
    json_data = []
    for record in answer:
        json_data.append(record['n'])
    json_data = json_data[(page - 1) * 10:page * 10]
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)


def drug_info(request):
    return render(request, 'medical_info/drug_info.html')


def get_drug_info(request):
    page = request.GET.get('page')
    page = int(page)
    answer = g.run(
        "MATCH (n:Drug) RETURN n LIMIT 50").data()
    json_data = []
    for record in answer:
        json_data.append(record['n'])
    # 返回JSON响应
    json_data = json_data[(page - 1) * 10:page * 10]
    return JsonResponse(json_data, safe=False)

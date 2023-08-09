from django.http import JsonResponse
from django.shortcuts import render
from medical.settings import g

def symptom_info(request):
    return render(request, 'medical_info/symptom_info.html')
def get_symptom_info(request):
    answer = g.run(
        "MATCH (n:Symptom) RETURN n").data()
    json_data = []
    for record in answer:
        json_data.append(record['n'])
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)


def get_select(request):
    department=request.GET.get('department')
    print(department)
    answer = g.run(
        "MATCH (n:Symptom)-[r:BELONGS_TO]->(p:Department{name:\"" + department + "\"}) RETURN n ").data()
    json_data = []
    for record in answer:
        json_data.append(record['n'])
    # 返回JSON响应
    return JsonResponse(json_data, safe=False)
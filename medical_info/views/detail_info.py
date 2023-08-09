from django.http import JsonResponse
from django.shortcuts import render
from medical.settings import g
import json


def drug_detail(request):
    item=request.GET.get('item')
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
    return render(request, 'medical_info/detail_info.html', {'data':json_data})

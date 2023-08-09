from django.http import JsonResponse
from django.shortcuts import render
from medical.settings import g
import json


def drug_detail(request, item):
    answer = g.run("MATCH (n) where n.name=\"" + item + "\" RETURN n").data()
    li1 = []
    li2 = []
    li2.append(answer[0]['n']['name'])
    for k in answer[0]['n']:
        if k != 'name':
            li1.append(k)
            li2.append(answer[0]['n'][k])
    # function = g.run("MATCH (n:{name:\"" + gn + "\"}) RETURN n.function").data()
    # side_effect = g.run("MATCH (n:{name:\"" + gn + "\"}) RETURN n.side_effect").data()
    # usage = g.run("MATCH (n:{name:\"" + gn + "\"}) RETURN n.usage").data()
    return render(request, 'medical_info/detail_info.html', {'ti': li1, 'list': li2})

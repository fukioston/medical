from django.http import JsonResponse
from django.shortcuts import render, redirect
from medical.local_settings import g


def statistic(request):
    graph = g
    Disease = graph.run("MATCH(m:Disease) RETURN COUNT(m)").data()[0]['COUNT(m)']
    Department = graph.run("MATCH(m:Department) RETURN COUNT(m)").data()[0]['COUNT(m)']
    Drug = graph.run("MATCH(m:Drug) RETURN COUNT(m)").data()[0]['COUNT(m)']
    Food = graph.run("MATCH(m:Food) RETURN COUNT(m)").data()[0]['COUNT(m)']
    Symptom = graph.run("MATCH(m:Symptom) RETURN COUNT(m)").data()[0]['COUNT(m)']
    li = [Disease, Department, Drug, Food, Symptom]
    return render(request, 'statistic/sta.html', {'list': li, })

import time
import pandas as pd
import csv
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

    neike = graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='内科' RETURN count(n)").data()[0][
        'count(n)']
    waike = graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='外科' RETURN count(n)").data()[0][
        'count(n)']
    fuchan = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='妇产科' RETURN count(n)").data()[0][
            'count(n)']
    chuanran = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='传染科' RETURN count(n)").data()[0][
            'count(n)']
    shengzhi = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='生殖健康' RETURN count(n)").data()[0][
            'count(n)']
    nanke = graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='男科' RETURN count(n)").data()[0][
        'count(n)']
    pifu = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='皮肤性病科' RETURN count(n)").data()[
            0][
            'count(n)']
    zhongyi = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='中医科' RETURN count(n)").data()[0][
            'count(n)']
    wuguan = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='五官科' RETURN count(n)").data()[0][
            'count(n)']
    jingshen = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='精神科' RETURN count(n)").data()[0][
            'count(n)']
    xinli = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='心理科' RETURN count(n)").data()[0][
            'count(n)']
    erke = graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='儿科' RETURN count(n)").data()[0][
        'count(n)']
    yingyang = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='营养科' RETURN count(n)").data()[0][
            'count(n)']
    zhongliu = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='肿瘤科' RETURN count(n)").data()[0][
            'count(n)']
    qita = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='其他科室' RETURN count(n)").data()[0][
            'count(n)']
    jizhen = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='急诊科' RETURN count(n)").data()[0][
            'count(n)']
    tijian = \
        graph.run("MATCH (n:Disease)-[:BELONGS_TO]->(m:Department) where m.name='体检科' RETURN count(n)").data()[0][
            'count(n)']
    ra = [neike, waike, fuchan, chuanran, shengzhi, nanke, pifu, zhongyi, wuguan, jingshen, xinli, erke,
          yingyang, zhongliu, qita, jizhen, tijian]

    d = []
    t = []
    data = pd.read_csv('../../rate.csv')
    # date = data['date']
    times = data['times']
    # for i in range(1, 6):
    #     d.append(str(date[len(date) - (6 - i)]))
    for i in range(1, 6):
        t.append(times[len(times) - (6 - i)])
    return render(request, 'statistic/sta.html', {'list': li, 'rate': ra, 'times': t, })


def p():
    data = pd.read_csv("../../rate.csv")
    t = time.strftime("%Y-%m-%d")
    date = data['date']
    l = len(date)
    if date[len(date) - 1] != t:
        l = l + 1
        af = {'date': [t], 'times': [0]}
        a = pd.DataFrame(af)
        with open('../../rate.csv', mode='a', newline='') as file:
            a.to_csv(file, header=(not file.tell()), index=False)

    with open('../../rate.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        d = list(reader)
        d[l][1] = str(int(d[l][1]) + 1)
    with open('../../rate.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # 写入数据
        writer.writerows(d)

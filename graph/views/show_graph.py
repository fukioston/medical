import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

import os

from graph.views.neo4j_db import neo4jconn
from user.models import UserInfo


def show(request):
    uinfo = request.session.get('info')
    user_id = uinfo['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    if query_set:
        return render(request, 'graph/graph.html',{'user_info':query_set})
    else:
        return render(request, 'graph/graph.html')



def handle(request):
    ctx = {}
    if request.GET:
        db = neo4jconn()
        entity1 = request.GET['entity1']
        relation = request.GET['relation']
        entity2 = request.GET['entity2']
        searchResult = {}

        # 若只输入entity1,则输出与entity1有直接关系的实体和关系
        if len(entity1) != 0 and len(relation) == 0 and len(entity2) == 0:
            searchResult = db.findRelationByEntity1(entity1)

        # 若只输入entity2则,则输出与entity2有直接关系的实体和关系
        if len(entity2) != 0 and len(relation) == 0 and len(entity1) == 0:
            searchResult = db.findRelationByEntity2(entity2)

        # 若输入entity1和relation，则输出与entity1具有relation关系的其他实体
        if len(entity1) != 0 and len(relation) != 0 and len(entity2) == 0:
            searchResult = db.findOtherEntities(entity1, relation)

        # 若输入entity2和relation，则输出与entity2具有relation关系的其他实体
        if len(entity2) != 0 and len(relation) != 0 and len(entity1) == 0:
            searchResult = db.findOtherEntities2(entity2, relation)

        # 全为空 则输出整个知识图谱
        if len(entity1) == 0 and len(relation) == 0 and len(entity2) == 0:
            searchResult = db.knowledgeGraph()

        # 全不为空，那就输出用户给定的那两个实体间的关系
        if len(entity1) != 0 and len(relation) != 0 and len(entity2) != 0:
            searchResult = db.findEntities1AndEntities2(entity1, entity2, relation)

        return JsonResponse(json.dumps(searchResult), json_dumps_params={'ensure_ascii': False},safe=False)

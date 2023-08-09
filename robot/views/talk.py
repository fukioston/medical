from django.http import JsonResponse
from django.shortcuts import render, redirect

from user.models import UserInfo
from utils.robot.get_answer import *
from statistic.views.vvv import p


def talk(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'robot/talk.html', {'user_info': query_set, })


def answer(request):
    p()
    message = '抱歉，您的问题我可能无法给出答复。请您把问题提的尽量准确一些。'
    question = request.GET.get('send_txt')
    # 如果表中有了数据就报错
    if classify(question, region_tree, wdtype_dict):
        message2 = search_main(parser_main(classify(question, region_tree, wdtype_dict)))
        print(classify(question, region_tree, wdtype_dict))
        message = message2
    return JsonResponse({'status': True, 'err': "无法回复", 'message': message})

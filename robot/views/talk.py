from django.http import JsonResponse
from django.shortcuts import render, redirect

from user.models import UserInfo


def talk(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'robot/talk.html', {'user_info': query_set, })


def answer(request):
    message = '抱歉，您的问题我可能无法给出答复。请您把问题提的尽量准确一些。'
    # 如果表中有了数据就报错
    return JsonResponse({'status': True, 'err': "已经收藏", 'message': message})

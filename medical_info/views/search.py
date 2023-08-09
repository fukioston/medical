from django.shortcuts import render

from user.models import UserInfo


def search(request):
    uinfo = request.session.get('info')
    user_id = uinfo['id']
    query_set = UserInfo.objects.filter(id=user_id).first()

    kw = request.GET.get('kw')  # 获取参数值
    # 用关键字搜索neo4j库
    print(kw)

    return render(request, 'medical_info/search.html', {'user_info': query_set})

from django.shortcuts import render

from user.models import UserInfo


def home(request):
    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'medical_info/home.html',{'user_info':query_set})
    else:
        return render(request, 'medical_info/home.html', )
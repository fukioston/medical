from django.http import JsonResponse
from django.shortcuts import render, redirect

from user.models import UserInfo
def mymanage(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    return render(request, 'column/manage.html', {'user_info': query_set, })
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from user.models import UserInfo


def apply_admin(request):
    return render(request,'user/apply_admin.html')
def satisfy(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    if query_set.identity=='user':
        return JsonResponse({'status': True,  })
    else:
        return JsonResponse({'status': False,  })
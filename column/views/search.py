from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from column.models import articles

from user.models import UserInfo


def search(request):
    uinfo = request.session.get('info')
    if uinfo:
        user_id = uinfo['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'column/search.html', {'user_info': query_set})
    return render(request, 'column/search.html')


def search_tip(request):
    kw = request.POST.get('kw')
    print(kw)
    article_objs = articles.objects.filter(article_name__contains=kw, status=1)
    article_name_list = [article_obj.article_name.strip() for article_obj in article_objs]
    article_name_list = list(set(article_name_list))
    if len(article_name_list) > 5:
        article_name_list = []
    print(article_name_list)

    return JsonResponse({'status': True, 'err': "无法回复", 'info': article_name_list})


def search_result(request):
    uinfo = request.session.get('info')
    kw = request.GET.get('kw')  # 获取参数值
    print(kw)
    article_objs = articles.objects.filter(article_name__contains=kw, status=1)
    if not article_objs:
        if uinfo:
            user_id = uinfo['id']
            query_set = UserInfo.objects.filter(id=user_id).first()
            return render(request, 'column/404.html', {'user_info': query_set})
        return render(request, 'column/404.html')
    articles_id = [article_obj.id for article_obj in article_objs]
    article_name_list = [article_obj.article_name for article_obj in article_objs]
    article_img_list = [article_obj.img_url for article_obj in article_objs]
    for i in range(len(article_img_list)):
        s = str(article_img_list[i])
        if s.__contains__('static'):
            article_img_list[i] = '/' + s
            print(article_img_list[i])

    article_uploader_img = [UserInfo.objects.filter(id=article_obj.uploader_id).first().profile_img
                            for article_obj in article_objs]
    article_uploader = [UserInfo.objects.filter(id=article_obj.uploader_id).first().username
                        for article_obj in article_objs]
    article_upload_time = [article_obj.upload_time for article_obj in article_objs]
    article_likes = [article_obj.likes for article_obj in article_objs]
    article_click = [article_obj.click for article_obj in article_objs]
    info = list(
        zip(article_name_list, article_img_list, article_uploader, article_upload_time, article_likes, article_click,
            articles_id, article_uploader_img))
    if uinfo:
        user_id = uinfo['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'column/article_list.html', {'info_list': info, 'user_info': query_set})
    else:
        return render(request, 'column/article_list.html', {'info_list': info})

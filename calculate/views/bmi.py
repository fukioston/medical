from django.http import JsonResponse
from django.shortcuts import render, redirect
from user.models import UserInfo
def get_suggestion(bmi):#这个去网上找建议
    if bmi<20:
        return True

def bmi_calculate(request):
    height=request.GET.get('height')
    height=float(height)
    weight=request.GET.get('weight')
    weight = float(weight)
    bmi=(weight/(height*height))*10000
    bmi=round(bmi, 2)
    print(bmi)
    bmi=str(bmi)
    message = '你的BMI为：'
    message=message+bmi
    # 如果表中有了数据就报错
    return JsonResponse({'status': True, 'err': "已经收藏", 'message': message})




def bmi(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    # on_sales_num = Items.objects.filter(userid=user_id).count()

    return render(request, 'calculate/bmi.html', {'user_info': query_set, })
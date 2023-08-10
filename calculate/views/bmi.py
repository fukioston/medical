from django.http import JsonResponse
from django.shortcuts import render, redirect,HttpResponse
from user.models import UserInfo


def get_suggestion(bmi):  # 这个去网上找建议
    if bmi < 18.5:
        return "（过瘦）。\n\n建议：\n- 增加营养摄入，确保足够的热量\n- 增加高蛋白质食物的摄入\n- 增加健康脂肪的摄入\n- 咨询医生或专业的营养师"
    elif bmi>=18.5 and bmi <24.0:
        return "（正常范围）。\n\n建议：\n- 保持健康的饮食习惯\n- 增加适量的体育锻炼\n- 定期进行体检"
    elif bmi>=24.0 and bmi<28.0:
        return "（超重）。\n\n建议：\n- 减少高热量食物的摄入\n- 增加有氧运动，控制体重\n- 避免过度饮食和不健康的生活习惯"
    elif bmi>=28.0 and bmi<34.9:
        return "（轻度肥胖）。\n\n建议：\n- 减少高热量、高脂肪食物的摄入\n- 增加适度的有氧运动和体力活动\n- 咨询专业医生或营养师，制定合适的减重计划"
    elif bmi>=34.9 and bmi<39.9:
        return "（中度肥胖）。\n\n建议：\n- 寻求医生的帮助，制定科学的减重方案\n- 控制饮食，适当增加运动量\n- 增强自我健康意识，避免不健康的饮食习惯"
    elif bmi>=39.9:
        return "（重度肥胖）。\n\n建议：\n- 立即寻求专业医生的帮助，制定科学的减重方案\n- 严格控制饮食，增加有氧运动和体力活动\n- 增强自我健康意识，树立正确的健康观念"


def bmi_calculate(request):
    height = request.GET.get('height')
    height = float(height)
    weight = request.GET.get('weight')
    weight = float(weight)
    bmi = (weight / (height * height)) * 10000
    bmi = round(bmi, 2)
    print(bmi)
    suggestion = get_suggestion(bmi)
    bmi = str(bmi)
    message = '您的BMI指数为：'
    message = message + bmi + suggestion
    # 如果表中有了数据就报错
    return JsonResponse({'status': True, 'err': "已经收藏", 'message': message})


def bmi(request):
    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'calculate/bmi.html', {'user_info': query_set, })
    else:
        return render(request, 'calculate/bmi.html',)
    # on_sales_num = Items.objects.filter(userid=user_id).count()


from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 0.排除那些不需要登录就能访问的页面
        #   request.path_info 获取当前用户请求的URL /login/
        if request.path_info in ['/user/login/',
                                 "/user/image/code/",
                                 '/user/register/',
                                 '/user/sms/code/',
                                 '/user/login/sms/',
                                 '/user/index/',
                                 '/user/logout',
                                 '/calculate/bmi/',
                                 '/calculate/bmi_cal',
                                 '/column/catalog',
                                 '/column/article_list',
                                 '/column/article',
                                 '/column/search',
                                 '/column/search_tip/',
                                 '/column/search_result',

                                 ]:
            return

        # 1.读取当前访问的用户的session信息，如果能读到，说明已登陆过，就可以继续向后走。
        info_dict = request.session.get("info")
        if info_dict:
            return
        # 2.没有登录过，重新回到登录页面
        return redirect('/user/login/')

"""second_hand_websites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from user.views import login, home, register, apply_admin

urlpatterns = [
    path('login/', login.login, name="login"),
    path('image/code/', login.image_code,name='image_code'),
    path('edit_info/', home.edit_info,name="edit_info"),
    path('sms/code/', login.send_sms,name="send_sms"),
    path('login/sms/', login.login_sms,name="login_sms"),
    path('home/', home.home,name="home"),
    path('register/',register.register,name="register"),
    path('image/code/',login.image_code,name='image_code'),
    path('logout/',home.logout,name="logout"),
    path('edit_pwd/',home.edit_pwd,name='edit_pwd'),
    path('apply_admin',apply_admin.apply_admin),
    path('satisfy',apply_admin.satisfy)

]


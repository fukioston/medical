"""medical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include('user.urls')),
    path("graph/", include('graph.urls')),
    path("robot/", include('robot.urls')),
    path("calculate/", include('calculate.urls')),
    path("column/", include('column.urls')),
    path("map/", include('map.urls')),
    path("statistic/", include('statistic.urls')),
    path("manager/", include('manager.urls')),
    path("statistic/", include('statistic.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('medical_info/', include('medical_info.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

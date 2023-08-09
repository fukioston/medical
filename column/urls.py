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
from column.views import catalog, search
from column.views import article_list
from column.views import upload

urlpatterns = [
    path('catalog', catalog.home, name='catalog.home'),
    path('article_list', catalog.article_list),
    path('article', article_list.article),
    path('upload', upload.upload),
    path('search', search.search),
    path('iscollect/', article_list.iscollect),
    path('click_favorite/', article_list.change_favorite),
    path('cancel_favorite/', article_list.cancel_favorite),
    path('search_tip/', search.search_tip),
    path('edit_article', upload.edit_article),
    path('show_collects', article_list.show_collects)
]

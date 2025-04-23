"""
    Blogアプリ
    URL定義

    Filename urls.py
    Date:2025.4.2
    written by:Hamada Jo

"""
from django.urls import path
from . import views

app_name='blog' #アプリケーション名
urlpatterns=[
    path('',views.post_list,name='post_list'),
]

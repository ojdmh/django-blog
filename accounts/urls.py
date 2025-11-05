"""
    Accountsアプリ
    URL定義

    Filename urls.py
    Date 2025.10.1
    Written by Hamadajo

"""
from django.urls import path
from . import views

app_name="accounts" #アプリケーション名
urlpatterns=[
    path('profile/<int:pk>',views.UserDetail.as_view(),name='user_detail'),
    path('profile/update/<int:pk>',views.UserUpdate.as_view(),name='user_update'),
]

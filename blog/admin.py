"""
    Blogアプリ
    admin用の設定

    Filename admin.py
    Date: 2025.4.2
    Written by Jo Hamada

"""
from django.contrib import admin
from .models import Post

admin.site.register(Post)

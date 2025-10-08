from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),#/adminを付け加えるとadmin.site.urlsに飛ぶ
    path("",include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]

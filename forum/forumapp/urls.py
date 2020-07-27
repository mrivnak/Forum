from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    re_path(r'category/(?P<id>\d+)', views.category, name='category'),
    re_path(r'post/(?P<id>\d+)', views.post, name='post'),
    re_path(r'user/(?P<id>\d+)', views.user, name='user'),
]
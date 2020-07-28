from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    re_path(r'^category/(?P<id>\d+)', views.category, name='category'),
    re_path(r'^post/(?P<id>\d+)', views.post, name='post'),
    re_path(r'^user/(?P<id>\d+)', views.user, name='user'),
    path('user/', views.error404, name='404'),
    re_path(r'^forms/(?P<type>\w+)/add', views.form_add, name='form_add'),
    re_path(r'^forms/(?P<type>\w+)/edit/(?P<id>\d+)', views.form_edit, name='form_edit'),
    re_path(r'^forms/(?P<type>\w+)/delete/(?P<id>\d+)', views.delete, name='delete'),
]
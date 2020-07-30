from django.urls import path, re_path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views, forms

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', include('django.contrib.auth.urls')), #default logout url/view --> redirect to home
    path('login/', auth_views.LoginView.as_view(authentication_form=forms.LoginForm), name='login'),
    path('signup/', views.signup, name='signup'),
    re_path(r'^category/(?P<id>\d+)', views.category, name='category'),
    re_path(r'^post/(?P<id>\d+)', views.post, name='post'),
    re_path(r'^user/(?P<id>\d+)', views.user, name='user'),

    re_path(r'^forms/(?P<type>\w+)/add', views.form_add, name='form_add'),
    re_path(r'^forms/(?P<type>\w+)/add/(?P<id>\d+)', views.form_add_id, name='form_add_id'),
    re_path(r'^forms/(?P<type>\w+)/edit/(?P<id>\d+)', views.form_edit, name='form_edit'),
    re_path(r'^forms/(?P<type>\w+)/delete/(?P<id>\d+)', views.delete, name='delete'),
]

handler404 = 'forumapp.views.page_not_found'
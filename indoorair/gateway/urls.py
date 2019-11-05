"""
homepage/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_page, name='register_page'),
    path('register/success', views.register_success_page, name='register_success_page'),
    path('login', views.login_page, name='login_page'),
    path('api/regsiter', views.post_register_api, name='register_api'),
    path('api/login', views.post_login_api, name='login_api'),
]

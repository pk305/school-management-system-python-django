# -*- encoding: utf-8 -*-
from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('home', views.index, name='index_home'),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]

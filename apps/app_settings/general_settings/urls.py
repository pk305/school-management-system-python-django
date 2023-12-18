# -*- encoding: utf-8 -*-
from django.urls import path
from .views import general_list

urlpatterns = [
    path("", general_list, name='general'),
]

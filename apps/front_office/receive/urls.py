# -*- encoding: utf-8 -*-
from django.urls import path
from .views import receive_list

urlpatterns = [
    path("", receive_list, name='receive'),
]

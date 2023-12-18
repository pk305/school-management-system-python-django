# -*- encoding: utf-8 -*-
from django.urls import path
from .views import complaint_list

urlpatterns = [
    path("", complaint_list, name='complaint'),
]

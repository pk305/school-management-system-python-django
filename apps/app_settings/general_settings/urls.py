# -*- encoding: utf-8 -*-
from django.urls import path
from .views import general_list, ajax_schedit

urlpatterns = [
    path("", general_list, name='general'),
    path('ajax_schedit/', ajax_schedit, name='ajax_schedit'),
]

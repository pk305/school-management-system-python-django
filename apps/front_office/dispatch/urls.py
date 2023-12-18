# -*- encoding: utf-8 -*-
from django.urls import path
from .views import dispatch_list

urlpatterns = [
    path("", dispatch_list, name='dispatch'),
]

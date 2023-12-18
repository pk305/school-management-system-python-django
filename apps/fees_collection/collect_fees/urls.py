# -*- encoding: utf-8 -*-
from django.urls import path
from .views import fees_list

urlpatterns = [
    path("", fees_list, name='collect_fees'),
]

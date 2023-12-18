# -*- encoding: utf-8 -*-
from django.urls import path
from .views import general_call

urlpatterns = [
    path("", general_call, name='general-call'),
]

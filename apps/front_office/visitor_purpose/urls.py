# -*- encoding: utf-8 -*-
from django.urls import path
from .views import visitor_purpose_list

urlpatterns = [
    path("", visitor_purpose_list, name='visitor-purpose'),
]

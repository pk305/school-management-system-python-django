# -*- encoding: utf-8 -*-
from django.urls import path
# from .views import VisitorListView
from .views import visitors

urlpatterns = [
    path("", visitors, name='visitors'),
]

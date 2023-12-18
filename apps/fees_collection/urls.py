# -*- encoding: utf-8 -*-
from django.urls import path, include


urlpatterns = [
    path("collect/", include("apps.fees_collection.collect_fees.urls")),
]

# -*- encoding: utf-8 -*-
from django.urls import path, include


urlpatterns = [
    path("details/", include("apps.student_information.student_details.urls")),
]

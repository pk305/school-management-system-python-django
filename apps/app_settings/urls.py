# -*- encoding: utf-8 -*-
from django.urls import path, include


urlpatterns = [
    path("general/", include("apps.app_settings.general_settings.urls")),
]

# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.authentication.urls")),
    path('front-office/', include("apps.front_office.urls")),
    path('settings/', include("apps.app_settings.urls")),
    path("student-information/",
         include("apps.student_information.urls")),
    path("fees-collection/",
         include("apps.fees_collection.urls")),
    # Auth routes - login / register
    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]

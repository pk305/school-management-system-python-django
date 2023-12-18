# -*- encoding: utf-8 -*-
from django.urls import path, include


urlpatterns = [
    path("enquiry/", include("apps.front_office.enquiry.urls")),
    path("visitors", include("apps.front_office.visitor.urls")),
    path("general-call", include("apps.front_office.general_call.urls")),
    path("dispatch", include("apps.front_office.dispatch.urls")),
    path("receive", include("apps.front_office.receive.urls")),
    path("complaint", include("apps.front_office.complaint.urls")),
    path("visitor-purpose", include("apps.front_office.visitor_purpose.urls")),
]

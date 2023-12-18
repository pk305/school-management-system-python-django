# -*- encoding: utf-8 -*-
from django.urls import path
from .views import enquiry_list, enquiry_create_view

urlpatterns = [
    path("", enquiry_list, name='enquiry'),
    path("create", enquiry_create_view, name="enquiry-create"),
    # path("create/", StudentCreateView.as_view(), name="student-create"),
    #  path("list", StudentListView.as_view(), name="student-list"),
    # path("<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    # path("<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    # path("delete/<int:pk>/", StudentDeleteView.as_view(), name="student-delete"),
    # path("upload/", StudentBulkUploadView.as_view(), name="student-upload"),
    # path("download-csv/", DownloadCSVViewdownloadcsv.as_view(), name="download-csv"),
]

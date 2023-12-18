from django.shortcuts import render
from ...front_office.enquiry.forms import EnquiryForm
from ...front_office.enquiry.models import Enquiry


def student_list(request):
    list = Enquiry.objects.all()
    form = EnquiryForm()

    return render(request, "student/student_list.html", {"list": list, "form": form})

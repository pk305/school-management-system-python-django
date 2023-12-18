from django.shortcuts import render
from ...front_office.enquiry.forms import EnquiryForm
from ...front_office.enquiry.models import Enquiry


def general_list(request):
    general_list = Enquiry.objects.all()
    form = EnquiryForm()

    return render(request, "general/general_list.html", {"general_list": general_list, "form": form})



from django.shortcuts import render
from ...front_office.enquiry.forms import EnquiryForm
from ...front_office.enquiry.models import Enquiry


def fees_list(request):
    list = Enquiry.objects.all()
    form = EnquiryForm()

    return render(request, "fees/fees_list.html", {"list": list, "form": form})

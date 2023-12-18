# -*- encoding: utf-8 -*-
from django.shortcuts import render


def general_call(request):
    success = False
    # enquiry_list = Enquiry.objects.all()

    return render(request, "general_call/general_call_list.html", {"enquiry_list": {}, "success": success})

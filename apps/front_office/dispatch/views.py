from django.shortcuts import render


def dispatch_list(request):
    return render(request, "dispatch/dispatch_list.html", {"enquiry_list": {}, "success": True})

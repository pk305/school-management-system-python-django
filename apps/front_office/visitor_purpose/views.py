from django.shortcuts import render


def visitor_purpose_list(request):
    return render(request, 'visitor_purpose/visitor_purpose_list.html', {"visitor_purpose": {}})

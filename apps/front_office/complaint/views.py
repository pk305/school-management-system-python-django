from django.shortcuts import render


def complaint_list(request):
    return render(request, 'complaint/complaint_list.html', {'complaint_list': {}})

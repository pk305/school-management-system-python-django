from django.shortcuts import render


def receive_list(request):
    return render(request, 'receive/receive_list.html', {'receive': {}})

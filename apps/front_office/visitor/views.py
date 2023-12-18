from django.views.generic import ListView
from django.http import HttpResponse
import datetime
from django.shortcuts import render


# class VisitorListView(ListView):
#     context_object_name = "visitors_list"

def visitors(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return render(request, "visitor/visitor_list.html", {"context": html})

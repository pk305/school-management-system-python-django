from django.shortcuts import render
from .models import Enquiry
from .forms import EnquiryForm
from django.shortcuts import redirect
from django.contrib import messages


def enquiry_list(request):
    enquiry_list = Enquiry.objects.all()
    form = EnquiryForm()

    return render(request, "enquiry/enquiry_list.html", {"enquiry_list": enquiry_list, "form": form})


def enquiry_create_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = EnquiryForm(request.POST)

        if form.is_valid():
            e1 = Enquiry.objects.create(
                name=form.cleaned_data.get('name_add'),
                contact=form.cleaned_data.get('contact'),
                address=form.cleaned_data.get('address'),
                date=form.cleaned_data.get('date'),
                description=form.cleaned_data.get('description'),
                follow_up_date=form.cleaned_data.get('follow_up_date'),
                source=form.cleaned_data.get('source'),
                email=form.cleaned_data.get('email'),
                assigned=form.cleaned_data.get('assigned'),
                school_class=form.cleaned_data.get('current_class'),
                no_of_child=form.cleaned_data.get('no_of_child'),
                reference=form.cleaned_data.get('reference'),
                status="active",
                note=form.cleaned_data.get('note'),
            )
            if (e1):
                success_message = 'New Admission Enquiry created successfully'
                messages.success(request, success_message)

                return redirect('general')
    else:
        form = EnquiryForm()

    return render(request, "enquiry/enquiry_add.html", {"form": form, "success": success})

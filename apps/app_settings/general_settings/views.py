from django.shortcuts import render
from ...front_office.enquiry.forms import EnquiryForm
from ...front_office.enquiry.models import Enquiry
from .forms import GenSettingForm
from django.http import JsonResponse
from django.contrib import messages
from .models import SchSettings


def general_list(request):
    general_list = Enquiry.objects.all()
    form = EnquiryForm()
    Genform = GenSettingForm()
    messages = {'success': True}
    return render(request, "general/general_list.html", {"general_list": general_list, "form": form, "messages": messages})


def ajax_schedit(request):
    if request.method == 'POST':
        # form = GenSettingForm(request.POST)
        sch_name = request.POST.get('sch_name')
        sch_dise_code = request.POST.get('sch_dise_code')
        base_url = request.POST.get('base_url')
        currency_format = request.POST.get('currency_format')
        folder_path = request.POST.get('folder_path')
        currency_place = request.POST.get('currency_place')
        sch_address = request.POST.get('sch_address')
        sch_date_format = request.POST.get('sch_date_format')
        sch_email = request.POST.get('sch_email')
        sch_id = request.POST.get('sch_id')
        sch_phone = request.POST.get('sch_phone')
        sch_session_id = request.POST.get('sch_session_id')
        sch_start_month = request.POST.get('sch_start_month')
        sch_start_week = request.POST.get('sch_start_week')
        sch_timezone = request.POST.get('sch_timezone')

        # Validate the data if necessary

        try:
            sett = request.POST
            sett = SchSettings.objects.create(
                name=sch_name,
                dise_code=sch_dise_code,
                # base_url=base_url,
                # currency_format=currency_format,
                # currency_place=currency_place,
                # folder_path=folder_path,
                address=sch_address,
                date_format=sch_date_format,
                email=sch_email,
                # sch_id=sch_id,
                phone=sch_phone,
                session_id=sch_session_id,
                # sch_start_month=sch_start_month,
                # sch_start_week=sch_start_week,
                timezone=sch_timezone)

            return JsonResponse({'status': 'success', 'message': 'School saved successfully.', 'data': sett})
        except Exception as e:
            return JsonResponse({'status': 'error', 'errors': str(e)})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

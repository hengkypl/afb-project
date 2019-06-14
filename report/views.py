from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

from alatberat.models import Hourmeter

from .forms import HourmeterReportForm
from .utils import indo_date_to_iso


# Create your views here.
class ReportIndexView(TemplateView):
    template_name = 'report/report_index.html'


class HourmeterReportView(ListView):
    template_name = 'report/report_hour_meter.html'
    model = Hourmeter
    valid_keys = ['alatid', 'operatorid', 'start_date', 'end_date']

    def get_queryset(self):
        queryset = None
        get_var = self.request.GET

        if get_var:

            # Ensure all parameters are not empty
            if all(key in get_var for key in self.valid_keys):
                alat_id = get_var['alatid']
                operator_id = get_var['operatorid']
                start_date = indo_date_to_iso(get_var['start_date'])
                end_date = indo_date_to_iso(get_var['end_date'])

                queryset = self.model.objects.filter(
                    alatid_id=int(alat_id), operatorid_id=int(operator_id), tanggal__range=[start_date, end_date]
                )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        total = 0
        form = HourmeterReportForm

        if context['object_list']:
            for obj in context['object_list']:
                total += obj.jam
        context['total'] = total
        context['form'] = form
        return context

    def post(self, request):
        querystring = ""
        post_var = request.POST

        if post_var:
            if all(key in post_var for key in self.valid_keys):
                form = HourmeterReportForm(data=post_var)
                if form.is_valid():
                    alatid = form.cleaned_data['alatid']
                    operatorid = form.cleaned_data['operatorid']
                    start_date = form.cleaned_data['start_date']
                    end_date = form.cleaned_data['end_date']

                    querystring = "?alatid={}&operatorid={}&start_date={}&end_date={}".format(
                        alatid, operatorid, start_date, end_date
                    )
                else:
                    messages.add_message(request, messages.ERROR, form.errors)

        return HttpResponseRedirect(reverse('report:hour_meter') + querystring)

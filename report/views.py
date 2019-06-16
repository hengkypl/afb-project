from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView


from alatberat.models import Bbmab, Biayaab, Hourmeter
from bbm.models import Transaksitangkiinduk, Transaksimobiltangki

from .forms import HourmeterReportForm, BiayaPerAlatReportForm, BiayaPerTanggalReportForm, BBMReportForm
from .forms import TransaksiTangkiIndukForm, TransaksiMobilTangkiForm


"""
REPORT INDEX
"""


class ReportIndexView(TemplateView):
    template_name = 'report/report_index.html'


"""
REPORT ALAT BERAT
"""


class HourmeterReportView(ListView):
    template_name = 'report/report_transaksi_tangki_induk.html'
    model = Hourmeter
    valid_keys = ['alatid', 'operatorid', 'start_date', 'end_date']
    prefilled_keys = ['alatid', 'operatorid']
    form = HourmeterReportForm

    def get_queryset(self):
        queryset = None
        get_var = self.request.GET

        if get_var:
            # Ensure all parameters are not empty
            if all(key in get_var for key in self.valid_keys):
                alat_id = get_var['alatid']
                operator_id = get_var['operatorid']
                start_date = get_var['start_date']
                end_date = get_var['end_date']

                queryset = self.model.objects.filter(
                    alatid_id=int(alat_id), operatorid_id=int(operator_id), tanggal__range=[start_date, end_date]
                )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        total_jam = 0
        total_hm_dunia = 0
        total_overtime = 0
        form_data = {}

        for key in self.prefilled_keys:
            try:
                form_data[key] = self.request.GET[key]
            except KeyError:
                pass
        form = self.form(data=form_data)

        if context['object_list']:
            for obj in context['object_list']:
                total_jam += obj.jam
                total_hm_dunia += obj.hmdunia
                total_overtime += obj.ot
        context['total_jam'] = total_jam
        context['total_hm_dunia'] = total_hm_dunia
        context['total_overtime'] = total_overtime
        context['form'] = form
        return context

    def post(self, request):
        querystring = ""
        post_var = request.POST

        if post_var:
            if all(key in post_var for key in self.valid_keys):
                form = self.form(data=post_var)
                if form.is_valid():
                    alatid = form.cleaned_data['alatid'].id
                    operatorid = form.cleaned_data['operatorid'].id
                    start_date = form.cleaned_data['start_date']
                    end_date = form.cleaned_data['end_date']

                    querystring = "?alatid={}&operatorid={}&start_date={}&end_date={}".format(
                        alatid, operatorid, start_date, end_date
                    )
                else:
                    messages.add_message(request, messages.ERROR, form.errors)

        return HttpResponseRedirect(reverse('report:hour_meter') + querystring)


class BiayaabPerAlatReportView(ListView):
    template_name = 'report/report_biaya_ab_alat.html'
    model = Biayaab
    valid_keys = ['alatid', 'start_date', 'end_date']
    prefilled_keys = ['alatid']
    form = BiayaPerAlatReportForm

    def get_queryset(self):
        queryset = None
        get_var = self.request.GET

        if get_var:
            # Ensure all parameters are not empty
            if all(key in get_var for key in self.valid_keys):
                alat_id = get_var['alatid']
                start_date = get_var['start_date']
                end_date = get_var['end_date']

                queryset = self.model.objects.filter(
                    alatid_id=int(alat_id), tanggal__range=[start_date, end_date]
                )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        total = 0
        form_data = {}

        for key in self.prefilled_keys:
            try:
                form_data[key] = self.request.GET[key]
            except KeyError:
                pass
        form = self.form(data=form_data)

        if context['object_list']:
            for obj in context['object_list']:
                total += obj.biaya
        context['total'] = total
        context['form'] = form
        return context

    def post(self, request):
        querystring = ""
        post_var = request.POST

        if post_var:
            if all(key in post_var for key in self.valid_keys):
                form = self.form(data=post_var)
                if form.is_valid():
                    alatid = form.cleaned_data['alatid'].id
                    start_date = form.cleaned_data['start_date']
                    end_date = form.cleaned_data['end_date']

                    querystring = "?alatid={}&start_date={}&end_date={}".format(
                        alatid, start_date, end_date
                    )
                else:
                    messages.add_message(request, messages.ERROR, form.errors)

        return HttpResponseRedirect(reverse('report:biaya_per_alat') + querystring)


class BiayaabPerTanggalReportView(ListView):
    template_name = 'report/report_biaya_ab_tanggal.html'
    model = Biayaab
    valid_keys = ['start_date', 'end_date']
    form = BiayaPerTanggalReportForm

    def get_queryset(self):
        queryset = None
        get_var = self.request.GET

        if get_var:
            # Ensure all parameters are not empty
            if all(key in get_var for key in self.valid_keys):
                start_date = get_var['start_date']
                end_date = get_var['end_date']

                queryset = self.model.objects.filter(
                    tanggal__range=[start_date, end_date]
                )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        total = 0

        if context['object_list']:
            for obj in context['object_list']:
                total += obj.biaya
        context['total'] = total
        context['form'] = self.form
        return context

    def post(self, request):
        querystring = ""
        post_var = request.POST

        if post_var:
            if all(key in post_var for key in self.valid_keys):
                form = self.form(data=post_var)
                if form.is_valid():
                    start_date = form.cleaned_data['start_date']
                    end_date = form.cleaned_data['end_date']

                    querystring = "?start_date={}&end_date={}".format(
                        start_date, end_date
                    )
                else:
                    messages.add_message(request, messages.ERROR, form.errors)

        return HttpResponseRedirect(reverse('report:biaya_per_tanggal') + querystring)


class BBMabReportView(ListView):
    template_name = 'report/report_bbm_ab.html'
    model = Bbmab
    valid_keys = ['alatid', 'start_date', 'end_date']
    prefilled_keys = ['alatid']
    form = BBMReportForm

    def get_queryset(self):
        queryset = None
        get_var = self.request.GET

        if get_var:
            # Ensure all parameters are not empty
            if all(key in get_var for key in self.valid_keys):
                alat_id = get_var['alatid']
                start_date = get_var['start_date']
                end_date = get_var['end_date']

                queryset = self.model.objects.filter(
                    alatid_id=int(alat_id), tanggal__range=[start_date, end_date]
                )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        total_bbm = 0
        form_data = {}

        for key in self.prefilled_keys:
            try:
                form_data[key] = self.request.GET[key]
            except KeyError:
                pass
        form = self.form(data=form_data)

        if context['object_list']:
            for obj in context['object_list']:
                total_bbm += obj.ltrmasuk
        context['total_bbm'] = total_bbm
        context['form'] = form
        return context

    def post(self, request):
        querystring = ""
        post_var = request.POST

        if post_var:
            if all(key in post_var for key in self.valid_keys):
                form = self.form(data=post_var)
                if form.is_valid():
                    alatid = form.cleaned_data['alatid'].id
                    start_date = form.cleaned_data['start_date']
                    end_date = form.cleaned_data['end_date']

                    querystring = "?alatid={}&start_date={}&end_date={}".format(
                        alatid, start_date, end_date
                    )
                else:
                    messages.add_message(request, messages.ERROR, form.errors)

        return HttpResponseRedirect(reverse('report:bbm_ab') + querystring)


"""
REPORT BBM
"""


class TransaksiTangkiIndukReportView(ListView):
    template_name = 'report/report_transaksi_tangki_induk.html'
    model = Transaksitangkiinduk
    valid_keys = ['tangkiid', 'start_date', 'end_date']
    prefilled_keys = ['tangkiid']
    form = TransaksiTangkiIndukForm

    def get_queryset(self):
        queryset = None
        get_var = self.request.GET

        if get_var:
            # Ensure all parameters are not empty
            if all(key in get_var for key in self.valid_keys):
                tangkiid = get_var['tangkiid']
                start_date = get_var['start_date']
                end_date = get_var['end_date']

                queryset = self.model.objects.filter(
                    tangkiid_id=int(tangkiid), tanggal__range=[start_date, end_date]
                )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        total_masuk = 0
        total_keluar = 0
        total_amount = 0
        form_data = {}

        for key in self.prefilled_keys:
            try:
                form_data[key] = self.request.GET[key]
            except KeyError:
                pass
        form = self.form(data=form_data)

        if context['object_list']:
            for obj in context['object_list']:
                total_masuk += obj.masuk
                total_keluar += obj.keluar
                total_amount += obj.amount
        context['total_masuk'] = total_masuk
        context['total_keluar'] = total_keluar
        context['total_amount'] = total_amount
        context['form'] = form
        return context

    def post(self, request):
        querystring = ""
        post_var = request.POST

        if post_var:
            if all(key in post_var for key in self.valid_keys):
                form = self.form(data=post_var)
                if form.is_valid():
                    tangkiid = form.cleaned_data['tangkiid'].id
                    start_date = form.cleaned_data['start_date']
                    end_date = form.cleaned_data['end_date']

                    querystring = "?tangkiid={}&start_date={}&end_date={}".format(
                        tangkiid, start_date, end_date
                    )
                else:
                    messages.add_message(request, messages.ERROR, form.errors)

        return HttpResponseRedirect(reverse('report:transaksi_tangki_induk') + querystring)


class TransaksiMobilTangkiReportView(ListView):
    template_name = 'report/report_transaksi_mobil_tangki.html'
    model = Transaksimobiltangki
    valid_keys = ['mobilid', 'start_date', 'end_date']
    prefilled_keys = ['mobilid']
    form = TransaksiMobilTangkiForm

    def get_queryset(self):
        queryset = None
        get_var = self.request.GET

        if get_var:
            # Ensure all parameters are not empty
            if all(key in get_var for key in self.valid_keys):
                mobilid = get_var['mobilid']
                start_date = get_var['start_date']
                end_date = get_var['end_date']

                queryset = self.model.objects.filter(
                    mobilid_id=int(mobilid), tanggal__range=[start_date, end_date]
                )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        total_keluar = 0
        form_data = {}

        for key in self.prefilled_keys:
            try:
                form_data[key] = self.request.GET[key]
            except KeyError:
                pass
        form = self.form(data=form_data)

        if context['object_list']:
            for obj in context['object_list']:
                total_keluar += obj.keluar
        context['total_keluar'] = total_keluar
        context['form'] = form
        return context

    def post(self, request):
        querystring = ""
        post_var = request.POST

        if post_var:
            if all(key in post_var for key in self.valid_keys):
                form = self.form(data=post_var)
                if form.is_valid():
                    mobilid = form.cleaned_data['mobilid'].id
                    start_date = form.cleaned_data['start_date']
                    end_date = form.cleaned_data['end_date']

                    querystring = "?mobilid={}&start_date={}&end_date={}".format(
                        mobilid, start_date, end_date
                    )
                else:
                    messages.add_message(request, messages.ERROR, form.errors)

        return HttpResponseRedirect(reverse('report:transaksi_mobil_tangki') + querystring)

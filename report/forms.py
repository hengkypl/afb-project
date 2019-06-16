from django import forms

from alatberat.models import Hourmeter, Alatberat, Operatorab, Biayaab, Bbmab
from .utils import indo_date_to_iso

"""
ALAT BERAT FORM
"""

# Mixin for date range form
class DateRangeFormMixin(forms.Form):
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs = {'class': 'form-control mr-3', "placeholder": "Start Date"}
        self.fields['end_date'].widget.attrs = {'class': 'form-control mr-3', "placeholder": "End Date"}

    def clean_start_date(self):
        start_date = self.data['start_date']
        end_date = self.data['end_date']
        if start_date > end_date:
            raise forms.ValidationError('Mohon periksa kembali tanggal pencarian anda')
        return indo_date_to_iso(start_date)

    def clean_end_date(self):
        end_date = self.data['end_date']
        return indo_date_to_iso(end_date)


class HourmeterReportForm(DateRangeFormMixin, forms.ModelForm):
    class Meta:
        model = Hourmeter
        fields = ('alatid', 'operatorid')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alatid'].widget.attrs = {'class': 'form-control mr-3'}
        self.fields['operatorid'].widget.attrs = {'class': 'form-control mr-3'}
        self.fields['alatid'].queryset = Alatberat.objects.all()
        self.fields['operatorid'].queryset = Operatorab.objects.all()


class BiayaPerAlatReportForm(DateRangeFormMixin, forms.ModelForm):
    class Meta:
        model = Biayaab
        fields = ('alatid', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alatid'].widget.attrs = {'class': 'form-control mr-3'}
        self.fields['alatid'].queryset = Alatberat.objects.all()


class BiayaPerTanggalReportForm(DateRangeFormMixin):
    pass


# Inherit Biaya per alat form due to the similarity
class BBMReportForm(BiayaPerAlatReportForm):
    pass

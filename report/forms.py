from django import forms
from alatberat.models import Hourmeter, Alatberat, Operatorab


class HourmeterReportForm(forms.ModelForm):
    start_date = forms.DateField()
    end_date = forms.DateField()

    class Meta:
        model = Hourmeter
        fields = ('alatid', 'operatorid')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alatid'].widget.attrs = {'class': 'form-control mr-3'}
        self.fields['operatorid'].widget.attrs = {'class': 'form-control mr-3'}
        self.fields['start_date'].widget.attrs = {'class': 'form-control mr-3', "placeholder": "Start Date"}
        self.fields['end_date'].widget.attrs = {'class': 'form-control mr-3', "placeholder": "End Date"}
        self.fields['alatid'].queryset = Alatberat.objects.all()
        self.fields['operatorid'].queryset = Operatorab.objects.all()

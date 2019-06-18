from django import forms

from alatberat.models import Alatberat
from bbm.models import Mobiltangki, Tangkiinduk, Transaksimobiltangki, Transaksitangkiinduk
from kendaraanlain.models import Kendaraanlain


class TransaksitangkiindukAddForm(forms.ModelForm):
    class Meta:
        model = Transaksitangkiinduk
        fields = ('tanggal', 'tangkiid', 'masuk', 'mobilid', 'keluar', 'keterangan', 'amount')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['tangkiid'].queryset = Tangkiinduk.objects.all()
        self.fields['mobilid'].queryset = Mobiltangki.objects.all()


class TransaksimobilTangkiAddForm(forms.ModelForm):
    class Meta:
        model = Transaksimobiltangki
        fields = ('tanggal', 'mobilid', 'keluar', 'alatid', 'kendaraanid', 'keterangan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['mobilid'].queryset = Mobiltangki.objects.all()
        self.fields['alatid'].queryset = Alatberat.objects.all()
        self.fields['kendaraanid'].queryset = Kendaraanlain.objects.all()

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ReportIndexView.as_view(), name='index'),
    url(r'^hour_meter$', views.HourmeterReportView.as_view(), name='hour_meter'),
    url(r'^biaya_per_alat$', views.BiayaabPerAlatReportView.as_view(), name='biaya_per_alat'),
    url(r'^biaya_per_tanggal$', views. BiayaabPerTanggalReportView.as_view(), name='biaya_per_tanggal'),
    url(r'^bbm_alat_berat$', views.BBMabReportView.as_view(), name='bbm_ab'),
    url(r'^transaksi_tangki_induk$', views.TransaksiTangkiIndukReportView.as_view(), name='transaksi_tangki_induk'),
    url(r'^transaksi_mobil_tangki$', views.TransaksiMobilTangkiReportView.as_view(), name='transaksi_mobil_tangki'),
    url(r'^hasil_produksi$', views.ProduksiReportView.as_view(), name='hasil_produksi'),
]

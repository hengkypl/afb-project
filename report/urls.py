from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ReportIndexView.as_view(), name='index'),
    url(r'^hour_meter$', views.HourmeterReportView.as_view(), name='hour_meter'),
    url(r'^biaya_per_alat$', views.BiayaabPerAlatReportView.as_view(), name='biaya_per_alat'),
]

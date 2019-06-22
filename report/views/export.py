from io import BytesIO

from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

from report.views import HourmeterReportView, BiayaabPerAlatReportView


def get_current_datetime_string():
    now = datetime.now()
    now_string = now.strftime('%Y-%m-%d__%H:%M:%S')
    return now_string


class PDFRendererView(object):
    def get_title(self):
        title = self.title_prefix
        try:
            start_date = self.request.GET['start_date']
            end_date = self.request.GET['end_date']
            title = "{} {}-{}".format(title, start_date, end_date)
        except Exception:
            pass
        return title

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_title()
        context["inner_template_name"] = self.inner_template_name
        return context

    def render_to_response(self, context, **response_kwargs):
        if not self.object_list:
            return HttpResponseRedirect(self.request.META['HTTP_REFERER'])

        context['title'] = self.get_title()
        template = get_template('report/pdf_template.html')
        html = template.render(context)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            http_response = HttpResponse(response.getvalue(), content_type='application/pdf')
            http_response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(self.export_filename)
            return http_response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class HourMeterExportView(PDFRendererView, HourmeterReportView):
    inner_template_name = "report/report_hour_meter_inner.html"
    export_filename = "{}_Hour_Meter.pdf".format(get_current_datetime_string())
    title_prefix = "Hour Meter Report"


class BiayaabPerAlatExportView(PDFRendererView, BiayaabPerAlatReportView):
    inner_template_name = "report/report_biaya_ab_alatinner"
    export_filename = "{}_Biaya_AB_per_Alat.pdf".format(get_current_datetime_string())

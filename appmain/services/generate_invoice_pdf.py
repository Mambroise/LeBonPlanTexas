# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/customer_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa

from django.conf import settings
from ..models import Invoice
from ..services.company_service import CompanyService

class PdfHandler:
    @staticmethod
    def generate_invoice_pdf(invoice_id, method='inline'):
        invoice = Invoice.objects.get(pk=invoice_id)
        company_info = CompanyService.get_company_info()
        context = {
            "company_info": company_info,
            "trip_invoice": invoice,
        }
        html = render_to_string('pdf/invoice_pdf.html', context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'{method}; filename="invoice_{invoice.customer.first_name}_{invoice.customer.last_name}_{invoice.invoice_number}.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        return response

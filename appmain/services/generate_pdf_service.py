# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/customer_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from ..models import Invoice
from .company_service import CompanyService

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
    
    @staticmethod
    def generate_terms_of_sales_pdf(request,method='inline'):
        lang = request.META.get('HTTP_ACCEPT_LANGUAGE', 'en').split(',')[0]
        response = HttpResponse(content_type='application/pdf')
        context = {"pdf" : True}
        if lang.startswith('fr'):
            html = render_to_string("pdf/terms_of_sale_fr.html",context)
            response['Content-Disposition'] = f'{method}; filename="leBonPlanTexas_CGV.pdf"'
        elif lang.startswith('es'):
            pass
        else:
            pass
            # html = render_to_string("lebonplantexas/legal_terms/terms_of_sale_us.html")
            # response['Content-Disposition'] = f'{method}; filename="us_name_terms.pdf"'


        pisa_status = pisa.CreatePDF(html,dest=response)

        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        
        return response
# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/terms_of_sale_view.py
# Author : Morice
# ---------------------------------------------------------------------------


from ..services.generate_pdf_service import PdfHandler

def terms_of_sale_pdf(request,method='inline'):
    return PdfHandler.generate_terms_of_sales_pdf(request)

def invoice_pdf(request, invoice_id):
    return PdfHandler.generate_invoice_pdf(invoice_id, method='inline')
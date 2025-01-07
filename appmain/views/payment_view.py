# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/payment.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render
from django.http import HttpResponseForbidden
from ..services.invoice_service import InvoiceService

def payment_view(request):
    token = request.GET.get('token')
    # Vérification du token
    invoice, success = InvoiceService.check_token_validity(token)
    if not success:
        return HttpResponseForbidden("Lien expiré ou invalide.")

    # accept terms of use modal
    return render(request, 'lebonplantexas/terms_of_sale.html',{'invoice':invoice})

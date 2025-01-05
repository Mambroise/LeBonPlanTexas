# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/payment.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from ..services.invoice_service import InvoiceService

def payment_view(request):
    token = request.GET.get('token')
    print('in the view')
    # Vérification du token
    invoice, success = InvoiceService.check_token_validity(token)
    if not success:
        return HttpResponseForbidden("Lien expiré ou invalide.")

    # Redirection vers Stripe Checkout
    return redirect(f"/create-checkout-session/?invoice_id={invoice.id}")

# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/validate_terms.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.utils.translation import gettext as _
from ..models import Invoice

def validate_terms(request):
    if request.method == "POST":
        invoice_id = request.POST.get('invoice_id')
        accept_terms = request.POST.get('accept_terms')
        if not accept_terms:
            return HttpResponseBadRequest(_("Vous devez accepter les CGU."))
        
        invoice = get_object_or_404(Invoice, id=invoice_id)
        invoice.terms_accepted = True
        invoice.save()

        return redirect(f"/create-checkout-session/?invoice_id={invoice.id}")

# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/stripe_checkout_session.py
# Author : Morice
# ---------------------------------------------------------------------------


import stripe
from django.conf import settings
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden
from django.utils.translation import gettext as _

from ..models import Invoice

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    invoice_id = request.GET.get('invoice_id')
    invoice = get_object_or_404(Invoice, id=invoice_id)
    
    if not invoice.terms_of_sale_accepted:
        return HttpResponseForbidden(_("Vous devez accepter les CGV avant de payer."))
    
    # Get currency from the customer country
    currency = get_currency_for_customer(invoice.customer)
    
    try:
        # Create Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': currency,
                    'product_data': {
                        'name': _('Reglement du devis %s' % invoice.id),
                        'description': _('Client : %s' % invoice.customer)
                    },
                    'unit_amount': int(invoice.total * 100),  # En centimes
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f"{settings.DOMAIN}/checkout-success/?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{settings.DOMAIN}/checkout-cancelled/?invoice_id={invoice.id}",
            client_reference_id=str(invoice.id),
        )
        return redirect(session.url)
    except Exception as e:
        print(f"Erreur lors de la création de la session Stripe: {e}")
        return HttpResponse(_("Erreur lors de la création de la session Stripe: %s") % e, status=500)


COUNTRY_CURRENCY_MAP = {
    'US': 'usd',   # États-Unis
    'FR': 'eur',   # France
    'BE': 'eur',   # Belgique
    'CH': 'chf',   # Suisse
    'CA': 'cad',   # Canada
}

def get_currency_for_customer(customer):
    country_code = customer.country.code if customer.country else None
    return COUNTRY_CURRENCY_MAP.get(country_code, 'eur') 

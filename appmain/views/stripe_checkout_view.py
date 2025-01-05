import stripe
from django.conf import settings
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.utils.translation import gettext as _

from ..models import Invoice

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    invoice_id = request.GET.get('invoice_id')
    invoice = get_object_or_404(Invoice, id=invoice_id)

    try:
        # Create Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': f'Devis {invoice.id}',
                    },
                    'unit_amount': int(invoice.total * 100),  # En centimes
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f"{settings.DOMAIN}/payment-success/?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{settings.DOMAIN}/payment-cancelled/",
        )
        return redirect(session.url)
    except Exception as e:
        print(f"Erreur lors de la création de la session Stripe: {e}")
        return HttpResponse(f"Erreur lors de la création de la session Stripe: {e}", status=500)

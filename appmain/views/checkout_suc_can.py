# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/templates/lebonplantexas/checkout_suc_can.html
# Author : Morice
# ---------------------------------------------------------------------------


import stripe
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from ..models import Invoice

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout_success(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return render(request, "error.html", {"message": "Session ID manquant."})

    try:
        # retreive checkout session from Stripe
        session = stripe.checkout.Session.retrieve(session_id)
        
        # example of what can be used in the session
        payment_intent = session.payment_intent
        customer_email = session.customer_details.email
        invoice_id = session.client_reference_id  # if used when creating a session
        invoice = Invoice.objects.get(pk=invoice_id)
        invoice.is_paid = True
        invoice.is_paid_date = timezone.now()
        invoice.save()


        # Optionnel : récupérer plus de détails si nécessaire
        payment = stripe.PaymentIntent.retrieve(payment_intent)
        amount_paid = payment.amount_received / 100  # in euros

        return render(request, "lebonplantexas/checkout_success.html", {
            "trip_invoice": invoice,
            "customer_email": customer_email,
            "amount_paid": amount_paid,
        })

    except Exception as e:
        print(f'error : {str(e)}')
        return render(request, "error.html", {"message": f"Erreur : {str(e)}"})


def checkout_cancelled():
    pass
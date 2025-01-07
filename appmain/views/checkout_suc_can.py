# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/templates/lebonplantexas/checkout_suc_can.html
# Author : Morice
# ---------------------------------------------------------------------------


import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout_success(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return render(request, "error.html", {"message": "Session ID manquant."})

    try:
        # Récupérer la session de paiement depuis Stripe
        session = stripe.checkout.Session.retrieve(session_id)
        
        # Exemple d'informations disponibles dans la session
        payment_intent = session.payment_intent
        customer_email = session.customer_details.email
        invoice_id = session.client_reference_id  # Si utilisé lors de la création de la session
        
        # Optionnel : récupérer plus de détails si nécessaire
        payment = stripe.PaymentIntent.retrieve(payment_intent)
        amount_paid = payment.amount_received / 100  # En euros

        # Rendre une page de succès avec les détails
        return render(request, "checkout_success.html", {
            "invoice_id": invoice_id,
            "customer_email": customer_email,
            "amount_paid": amount_paid,
        })

    except Exception as e:
        return render(request, "error.html", {"message": f"Erreur : {str(e)}"})


def checkout_cancelled():
    pass
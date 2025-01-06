# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/stripe_webhook.py
# Author : Morice
# ---------------------------------------------------------------------------





from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import stripe

from ..models import Invoice 

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        # Vérification de l’authenticité de l’événement Stripe
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return JsonResponse({'status': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({'status': 'Invalid signature'}, status=400)

    # Gérer les différents types d'événements
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        invoice_id = session.get('client_reference_id')  # ID de la facture passé lors de la création de la session
        
        if invoice_id:
            try:
                # Marquer la facture comme payée
                invoice = Invoice.objects.get(id=invoice_id)
                invoice.is_paid = True
                invoice.save()
            except Invoice.DoesNotExist:
                return JsonResponse({'status': 'Invoice not found'}, status=404)

    return JsonResponse({'status': 'success'}, status=200)

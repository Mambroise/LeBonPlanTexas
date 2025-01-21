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
from django.utils.translation import gettext_lazy as _

from ..models import Invoice
from ..services.generate_invoice_pdf import PdfHandler
from ..services.send_email import send_checkout_success_email
from ..services.company_service import CompanyService

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout_success(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        message = _("Session ID manquant.")
        return render(request, "error.html", {"message": message})

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
        invoice.stripe_session_id = session_id
        invoice.save()

        #  mailing the invoice to the customer
        if not send_checkout_success_email(invoice):
            return render(request, "error.html", {"message": "Erreur email envoi facture"})

        # Optionnel : récupérer plus de détails si nécessaire
        payment = stripe.PaymentIntent.retrieve(payment_intent)
        amount_paid = payment.amount_received / 100  # in euros
        company_info = CompanyService.get_company_info()

        context = {
            "company_info": company_info,
            "trip_invoice": invoice,
            "customer_email": customer_email,
            "amount_paid": amount_paid,
        }

        return render(request, "lebonplantexas/checkout_success.html", context)

    except Exception as e:
        print(f'error : {str(e)}')
        message = _("Error : %s" % {str(e)})
        return render(request, "error.html", {"message": f"Erreur : {str(e)}"})


def checkout_cancelled(request):
    invoice_id = request.GET.get('invoice_id')
    if not invoice_id:
        message = _("L'attribut invoice_id absent de la requête")
        return render(request,'error.html', {'message' : message})
    try:
        invoice = Invoice.objects.get(pk=invoice_id)
        company_info = CompanyService.get_company_info()
    except Exception as e:
        message = _('Erreur : %s' % {str(e)})
        return render(request,'error.html', {'message' : message})
    
    context = {
            "company_info": company_info,
            "trip_invoice": invoice,
        }
    
    return render(request, "lebonplantexas/checkout_cancelled.html", context)

def print_invoice(request, invoice_id):
    return PdfHandler.generate_invoice_pdf(invoice_id, method='inline')